from django.shortcuts import render, redirect
from django.http import HttpResponse
from candidates.models.User import User
from functools import wraps


def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        role = 'admin'
        try:
            status = User.objects.get(
                email=email, password=password, role=role)
            request.session['admin_logged'] = True
            request.session['admin_data'] = {
                'email': email,
                'id': status.id
            }

            if request.POST.get('next') is not '':
                return redirect(request.POST['next'])
            return redirect('admin_dashboard')
        except User.DoesNotExist:
            return HttpResponse('failed')
    elif request.method == 'GET':
        next = request.GET.get('next', '')
        return render(request, 'auths/login.html', { 'next': next })


def logout(request):
    del request.session['admin_logged']
    del request.session['admin_data']
    return redirect('admin_login')


# Decorator for requiring authentication
def require_login(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if request.session.get('admin_logged') is None:
            return redirect(f'login?next={request.path}')
        return f(request, *args, **kwargs)
    return decorated_function
