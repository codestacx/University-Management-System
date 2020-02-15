from django.urls import path

from candidates import views


#use Auth Login Controller

from candidates.Controllers.auths import Auth
from candidates.Controllers.candidates import Candidate
from candidates.Controllers.Email import sendMail

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',Candidate.index,name='index'),
    path('login/',Auth.login,name='login'),
    path('logout/',Auth.logout,name='logout'),
    path('register_user/',Auth.signup,name='signup'),
    path('sendemail/',sendMail.email_confirmation,name='sendmail'),
    path('verifymail',sendMail.verifyEmail,name='verifymail'),
    path('resetpasswords/',sendMail.resetPassword,name='resetpasswords'),
    path('confirmresetpassword/<int:user_id>',sendMail.resetPassword,name='confirmresetpassword' ),
    path('submitresetpassword',sendMail.submitResetPassword,name='submitresetpassword'),
    path('testing/',views.testing,name='testing'),


]