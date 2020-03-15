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
def testing(request):
    #objectQuerySet = CandidateProfile.objects.filter(candidate_id=1)
    objectQuerySet = Qualification.objects.raw("SELECT * FROM `candidates_qualification`"
"LEFT JOIN `candidates_degreecriteria` ON `candidates_degreecriteria`.`degree_criteria_id` = `candidates_qualification`.`criteria_id`"
"WHERE `candidates_qualification`.`candidate_id` =1")


    data = serializers.serialize('json', list(objectQuerySet))
    return HttpResponse((data))
    # data = Qualification.objects.raw("SELECT * FROM `candidates_qualification` WHERE `candidates_qualification`.`candidate_id` =1")
    #
    # return HttpResponse({"data":list(json.dumps(data))})
