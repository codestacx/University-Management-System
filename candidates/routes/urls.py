from django.urls import path

from candidates import views


#use Auth Login Controller

from candidates.Controllers.auths import Auth
from candidates.Controllers.candidates import Candidate
from candidates.Controllers.Email import sendMail

from candidates.Controllers.candidates import Profile

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    # Auth Routes
    path('',Candidate.index,name='index'),
    path('login/',Auth.login,name='login'),
    path('logout/',Auth.logout,name='logout'),
    path('register_user/',Auth.signup,name='signup'),
    path('sendemail/',sendMail.email_confirmation,name='sendmail'),
    path('verifymail',sendMail.verifyEmail,name='verifymail'),
    path('resetpasswords/',sendMail.resetPassword,name='resetpasswords'),
    path('confirmresetpassword/<int:user_id>',sendMail.resetPassword,name='confirmresetpassword' ),
    path('submitresetpassword',sendMail.submitResetPassword,name='submitresetpassword'),



    # Entry Test routes
    path('testing/',views.testing,name='testing'),
    path("entry-test-application", views.entry_test_application, name='entry_test_application'),
    path("registeration-slip", views.registeration_slip, name='registeration_slip'),
    path("adjust-test-schedule", views.adjust_test_schedule, name='adjust_test_schedule'),
    path("entry-test-result", views.entry_test_result, name='entry_test_result'),


    #Profile routes

    path('personal-info',Profile.personalInfo,name='personal-info'),
    path('password-info',Profile.passwordInfo,name='password-info'),



]