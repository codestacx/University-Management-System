from django.shortcuts import render,redirect
from django.http import HttpResponse
from candidates.models.User import User
from candidates.models.CandidateProfile import CandidateProfile

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        role = 'admin'
        try:
            status = User.objects.get(email = email,password=password,role=role)
            request.session['admin_logged'] = True
            request.session['admin_data'] = {
                'email':email,
                'id':status.id
            }
            return redirect('home')
        except User.DoesNotExist:
            return HttpResponse('failed')
    return render(request,'auths/login.html')

def home(request):
    if request.session['admin_logged']:
        candidates = CandidateProfile.objects.all()
        return render(request, 'dashboard/candidates/index.html',{'candidates':candidates})
    else:
        return render(request,'auths/login.html')

def logout(request):

    del request.session['admin_logged']
    del request.session['admin_data']
    return render(request,'auths/login.html')