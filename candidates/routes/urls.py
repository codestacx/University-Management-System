from django.urls import path


#use Auth Login Controller

from candidates.Controllers.auths import Auth
from candidates.Controllers.candidates import Candidate

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',Candidate.index,name='index'),
    path('login/',Auth.login,name='login'),
    path('logout/',Auth.logout,name='logout')

]