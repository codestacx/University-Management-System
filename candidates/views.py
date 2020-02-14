from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from candidates.Controllers.Email import sendMail
from candidates.models.VerificationCode import VerificationCode
import json
def testing(request):
    email=request.POST['email']
    code = request.POST['code']
    count = VerificationCode.objects.filter(email=email,code=code).count()
    status = True if count>0 else False
    obj={
        "status":status
    }
    return HttpResponse(json.dumps(obj), content_type="application/json", status=200)