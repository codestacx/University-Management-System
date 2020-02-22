from django.shortcuts import render
from candidates.models.Degree import Degree
from candidates.models.CandidateProfile import CandidateProfile

from candidates.models.SittingPlan import *
from candidates.models.EntryTest import *

import io
from reportlab.pdfgen import  canvas
from django.http import FileResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import json

#import AppliedCandidate Models
from candidates.models.EntryTest import AppliedCandidate

def entry_test_application(request):
    if request.method == 'POST':

        candidate_id = request.POST['candidate_id']
        degree_id = request.POST['degree_id']

        done = AppliedCandidate.objects.create(candidate_id=candidate_id,degree_id=degree_id,challan_status=0)
        status = True if done else False
        return HttpResponse(json.dumps({
            'status':status
        }), content_type="application/json", status=200)

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
    template_src = 'challan.html'

    template = get_template(template_src)
    html = template.render({'name': name})
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')

    return 'lolz'
