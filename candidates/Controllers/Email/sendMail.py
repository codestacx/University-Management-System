from django.conf import settings
from django.core.mail import *
from django.urls import reverse
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
import json
from django.shortcuts import render,redirect
from django.utils.html import strip_tags
from django.contrib import messages
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
        elif VerificationCode.objects.filter(email=email,status=1).count()>0:
            count=-2
            msg="Email already verified"
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
            to_email = [email]
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
    VerificationCode.objects.filter(email=email).update(status=1)
    obj={
        "status":status
    }
    return HttpResponse(json.dumps(obj), content_type="application/json", status=200)


def resetPassword(request,user_id=None):
    if request.method=='POST':
        email = request.POST['email']
        obj={
            "status":0,
            "msg":None
        }
        if not isEmailExists(email):
            obj['msg']="No email found !"
        else:
            u = User.objects.filter(email=email).get()
            subject = 'Reset Credentials'
            link = "http://127.0.0.1:8000%s" % reverse('confirmresetpassword',kwargs={'user_id': u.pk})
            html_message = render_to_string('email/reset_password.html',{'link':link})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.EMAIL_HOST_USER]
            count = send_mail(subject, plain_message, from_email, to_email, html_message=html_message)
            obj['msg']="Confirmation link sent to your email"
            obj['status']=count
        return HttpResponse(json.dumps(obj), content_type='application/json', status=200)
    else:
        id  = user_id
        return render(request,'pages/login/resetPassword.html',{'id':id})



def isEmailExists(email):
    count = User.objects.filter(email__iexact=email).count()
    return True if count > 0 else False

def submitResetPassword(request):
    password = request.POST['password']
    id = request.POST['user_id']
    status = User.objects.filter(id=id).update(password=password)
    if(status>0):
        messages.error(request, 'Password updated successfully')
        return render(request, 'pages/login/login.html')




