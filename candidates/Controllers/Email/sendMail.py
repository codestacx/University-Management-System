from django.conf import settings
from django.core.mail import *
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
import json
from django.utils.html import strip_tags
import random
from candidates.models.VerificationCode import VerificationCode
from candidates.models.User import User

def email_confirmation(request):
    if(request.method=='POST'):
        email = request.POST['email']
        #check if already requested for same email
        if User.objects.filter(email=email).count()>0:
            count=-1
            msg="Email already registered"
        else:
            count = VerificationCode.objects.filter(email=email).count()
            if(count>0):
                querySet = VerificationCode.objects.filter(email=email).only('code')
                code = querySet[0].code
            else:
                code = random.randrange(100000,999999,5)
                VerificationCode(email=email,code=code).save()
            subject = 'Email Confirmation'
            html_message = render_to_string('email/email.html', {'code': code})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.EMAIL_HOST_USER]
            count = send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
            #count=1
            msg = "confirmation code sent to your email" if count> 0 else "Something goes wrong ! try again with another email"

        obj = {
            "msg": msg,
            "count": count
        }

    return HttpResponse(json.dumps(obj), content_type="application/json", status=200)

def verifyEmail(request):
    email=request.POST['email']
    code = request.POST['code']
    count = VerificationCode.objects.filter(email=email,code=code).count()
    status = True if count>0 else False
    obj={
        "status":status
    }
    return HttpResponse(json.dumps(obj), content_type="application/json", status=200)


