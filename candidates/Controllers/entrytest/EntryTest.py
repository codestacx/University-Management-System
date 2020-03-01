from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template

from candidates.models.User import User
from candidates.models.Degree import Degree
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.SittingPlan import *
from candidates.models.EntryTest import *
from candidates.models.WizardSession import WizardSession

import io
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
import json


def entry_test_application(request):
    if request.method == 'POST':
        try:
            degree_id = Degree.objects.get(degree_id=request.POST['degree'])
            candidate_id = User.objects.get(id=request.session['user_id'])
        except Degree.DoesNotExist:
            return HttpResponse('failure')
        
        print(request.POST)
        if request.POST['verification_status'] == 'on':
            candidate_application = AppliedCandidate.objects.create(
                candidate=candidate_id,
                paid_challan_copy=request.FILES['paid-challan-copy'],
                degree=degree_id
            )

            return HttpResponse(candidate_application.pk)
        else:
            return HttpResponse('failed')
    else:
        context = {}
        context['degrees'] = Degree.objects.all()
        context['current_user'] = CandidateProfile.objects.get(
            candidate_id=request.session['user_id'])

        return render(request, "pages/entrytest/entry_test_application.html", context=context)


def registeration_slip(request):
    return render(request, "pages/entrytest/registeration_slip.html")


def adjust_test_schedule(request):
    candidate_id = request.session['user_id']

    # get the info from parent table for requested candidate

    plan_info = PlanInfo.objects.get(candidate_id=candidate_id)

    # using hall id & slot id fetch hall and slot info

    hall_info = Hall.objects.get(hall_id=plan_info.hall_id)

    slot_info = Slot.objects.get(slot_id=plan_info.slot_id)

    test_info = TestTypes.objects.get(degree_id=(
        AppliedCandidate.objects.get(candidate_id=candidate_id).degree_id))

    context = {
        'plan_info': plan_info,
        'hall_info': hall_info,
        'slot_info': slot_info,
        'test_info': test_info
    }

    return render(request, "pages/entrytest/adjust_test_schedule.html", context=context)


def entry_test_result(request):
    candidate_id = request.session['user_id']

    data = EntryTestResult.objects.raw("SELECT * FROM `candidates_entrytestresult` INNER JOIN `candidates_testtypes` "
                                       "on `candidates_testtypes`.`test_id`=`candidates_entrytestresult`.`test_id` INNER JOIN  `candidates_degree` "
                                       "ON `candidates_degree`.`degree_id` = `candidates_testtypes`.`degree_id` WHERE `candidates_entrytestresult`.`candidate_id`=%s limit 1", [candidate_id])

    context = {
        'context': data[0]
    }

    return render(request, "pages/entrytest/entry_test_result.html", context=context)


def get_challan_pdf(request, name):
    template_src = 'pdf_templates/challan.html'

    template = get_template(template_src)
    html = template.render({'name': name})
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return 'lolz'


def wizard_session(request):
    if request.method == 'GET':
        if request.GET.get('degree', '') != '':
            ws = WizardSession.objects.filter(user_id=request.session['user_id'])
            if not ws:
                data = [{"degree": int(request.GET.get('degree', ''))}]
                data = json.dumps(data)
                x = WizardSession.objects.create(user_id=request.session['user_id'], data=data)
                return HttpResponse(json.dumps(x))
            else:
                ws = WizardSession.objects.get(user_id=request.session['user_id'])
                data = json.loads(ws.data)
                data['degree'] = int(request.GET.get('degree', ''))
                ws.data = json.dumps(data)
                ws.save()
                return HttpResponse(ws.data)
        elif request.GET.get('verification_status', '') != '':
            ws = WizardSession.objects.filter(user_id=request.session['user_id'])
            if not ws:
                data = [{"verification_status": request.GET.get('verification_status', '')}]
                data = json.dumps(data)
                x = WizardSession.objects.create(user_id=request.session['user_id'], data=data)
                return HttpResponse(json.dumps(x))
            else:
                ws = WizardSession.objects.get(user_id=request.session['user_id'])
                data = json.loads(ws.data)
                data['verification_status'] = request.GET.get('verification_status', '')
                ws.data = json.dumps(data)
                ws.save()
                return HttpResponse(ws.data)
        else:
            ws = WizardSession.objects.filter(user_id=request.session['user_id']).exists()
            
            if not ws:
                return HttpResponse(json.dumps("")) # nothing found
            else:
                ws = WizardSession.objects.get(user_id=request.session['user_id'])
                return HttpResponse(ws.data)
