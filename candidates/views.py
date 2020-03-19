from django.http import HttpResponse,JsonResponse
from django.template import RequestContext
from candidates.Controllers.Email import sendMail
from candidates.models.VerificationCode import VerificationCode
import json
import array
from candidates.models.PriorityDegree import *
from candidates.models.CandidateProfile import CandidateProfile
from django.shortcuts import render
from candidates.models.Degree import *
from django.core import serializers

from django.forms.models import model_to_dict

def testing(request):
    #objectQuerySet = CandidateProfile.objects.filter(candidate_id=1)
    objectQuerySet = Qualification.objects.raw("SELECT  `candidates_qualification`.`id`,`candidates_qualification`.`candidate_id`,`candidates_qualification`.`total_marks`,"
                                               "`candidates_qualification`.`obtained_marks`,`candidates_qualification`.`institute`,`candidates_qualification`.`passing_year`,"
                                               "`candidates_degreecriteria`.`requirement` as requirement FROM `candidates_qualification` LEFT JOIN `candidates_degreecriteria` ON `candidates_degreecriteria`.`degree_criteria_id`=`candidates_qualification`.`criteria_id`")

    x = objectQuerySet.__dict__

    #data = model_to_dict(objectQuerySet)

    return render(request,'testing/testing.html',{'data':objectQuerySet,'test':x})
    return JsonResponse((objects),safe=False)

    data = serializers.serialize('json', list(objectQuerySet))
    return HttpResponse((data))
    # data = Qualification.objects.raw("SELECT * FROM `candidates_qualification` WHERE `candidates_qualification`.`candidate_id` =1")
    #
    # return HttpResponse({"data":list(json.dumps(data))})
