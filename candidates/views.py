from django.http import HttpResponse,JsonResponse
from django.template import RequestContext
from candidates.Controllers.Email import sendMail
from candidates.models.VerificationCode import VerificationCode
import json
import array
from candidates.models.PriorityDegree import *
from django.shortcuts import render


def testing(request):
    degrees = PrioriyDegree.objects.all()
    priorities = []
    for i in range(1, 13):
        priorities.append(i)
    return render(request,'testing/testing.html',{'degrees':degrees,'priorities':priorities})
