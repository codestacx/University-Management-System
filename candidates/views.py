from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from candidates.Controllers.Email import sendMail
from candidates.models.VerificationCode import VerificationCode
import json


def testing(request):
    return render(request,'testing/testing.html')

def entry_test_application(request):
    return render(request, "pages/candidate/entry_test_application.html")

def registeration_slip(request):
    return render(request, "pages/candidate/registeration_slip.html")

def adjust_test_schedule(request):
    return render(request, "pages/candidate/adjust_test_schedule.html")

def entry_test_result(request):
    return render(request, "pages/candidate/entry_test_result.html")
