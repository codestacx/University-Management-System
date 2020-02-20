from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from candidates import views

from candidates.Controllers.auths import Auth
from candidates.Controllers.candidates import Candidate
from candidates.Controllers.Email import sendMail
from candidates.Controllers.entrytest import EntryTest

urlpatterns = [
    path('', Candidate.index, name='index'),
    path('login/', Auth.login, name='login'),
    path('logout/', Auth.logout, name='logout'),
    path('register_user/', Auth.signup, name='signup'),
    path('sendemail/', sendMail.email_confirmation, name='sendmail'),
    path('verifymail', sendMail.verifyEmail, name='verifymail'),
    path('testing/', views.testing, name='testing'),

    path("entry-test-application", EntryTest.entry_test_application, name='entry_test_application'),
    path("registeration-slip", EntryTest.registeration_slip, name='registeration_slip'),
    path("adjust-test-schedule", EntryTest.adjust_test_schedule, name='adjust_test_schedule'),
    path("entry-test-result", EntryTest.entry_test_result, name='entry_test_result'),
    path("get-challan-pdf/<str:name>", EntryTest.get_challan_pdf, name='get_challan_pdf')
]
