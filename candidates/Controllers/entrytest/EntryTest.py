from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template

from candidates.models.User import User
from candidates.models.Degree import Degree
from candidates.models.CandidateProfile import CandidateProfile
from candidates.models.SittingPlan import *
from candidates.models.EntryTest import *

import io
from reportlab.pdfgen import canvas
from xhtml2pdf import pisa
import json

def entry_test_application(request):
    if request.method == 'POST':
        # only challan copy uploaded
        if request.FILES:
            candidate_application = AppliedCandidate.objects.create(
                candidate=User.objects.get(id=request.session['user_id']),
                paid_challan_copy=request.FILES['paid-challan-copy']
            )

            return HttpResponse(candidate_application.pk)
        # form submitted excluding challan copy
        else:
            if request.POST['verification_status'] == 'on':
                candidate_application = AppliedCandidate.objects.get(candidate_id=request.session['user_id'])
                candidate_application.degree = Degree.objects.get(id=request.POST['degree'])
                candidate_application.save()

                return HttpResponse('success')
            else:
                return HttpResponse('failed')
    else:
        context = {}
        context['degrees'] = Degree.objects.all()
        context['current_user'] = CandidateProfile.objects.get(candidate_id=request.session['user_id'])
        
        return render(request, "pages/entrytest/entry_test_application.html", context=context)

def registeration_slip(request):
    return render(request, "pages/entrytest/registeration_slip.html")

def adjust_test_schedule(request):
    candidate_id = request.session['user_id']

    #get the info from parent table for requested candidate

    plan_info = PlanInfo.objects.get(candidate_id = candidate_id)

    #using hall id & slot id fetch hall and slot info

    hall_info = Hall.objects.get(hall_id = plan_info.hall_id)

    slot_info = Slot.objects.get(slot_id = plan_info.slot_id)

    test_info = TestTypes.objects.get(degree_id=(AppliedCandidate.objects.get(candidate_id=candidate_id).degree_id))


    context={
        'plan_info':plan_info,
        'hall_info':hall_info,
        'slot_info':slot_info,
        'test_info':test_info
    }


    return render(request, "pages/entrytest/adjust_test_schedule.html",context=context)


def entry_test_result(request):
    candidate_id = request.session['user_id']


    data = EntryTestResult.objects.raw("SELECT * FROM `candidates_entrytestresult` INNER JOIN `candidates_testtypes` "
    "on `candidates_testtypes`.`test_id`=`candidates_entrytestresult`.`test_id` INNER JOIN  `candidates_degree` "
    "ON `candidates_degree`.`degree_id` = `candidates_testtypes`.`degree_id` WHERE `candidates_entrytestresult`.`candidate_id`=%s limit 1",[candidate_id])


    context ={
        'context':data[0]
    }

    return render(request, "pages/entrytest/entry_test_result.html",context=context)

def get_challan_pdf(request, name):
    template_src = 'pdf_templates/challan.html'

    template = get_template(template_src)
    html  = template.render({'name': name})
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return 'lolz'
