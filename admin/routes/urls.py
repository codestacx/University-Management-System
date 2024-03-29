from django.urls import path
from admin.Controllers import AuthController
from admin.Controllers import CandidateController
from admin.Controllers import SittingPlan
from admin.Controllers import ChallanController
from admin.Controllers import EntryTestController
from admin.Controllers import QualificationController
from admin.Controllers import MeritListController
urlpatterns = [

    path('', CandidateController.dashboard, name='admin_dashboard'),

    # Authentication
    path('login/', AuthController.index, name='admin_login'),

    path('signout', AuthController.logout, name='admin_logout'),

    # entry test
    path('verify-candidate-profiles', CandidateController.verify_candidate_profile, name="verify_candidate_profile"),

    path('candidate/deactivate/<int:id>',CandidateController.deactivate_candidate,name='deactivate_candidate'),
    path('candidate/activate/<int:id>',CandidateController.activate_candidate,name='activate_candidate'),

    path('upload_hall', SittingPlan.uploadHall, name="upload_hall"),
    path('get-halls', SittingPlan.get_halls, name='get_halls'),
    path('upload_slot', SittingPlan.uploadSlot, name='upload_slot'),
    path('get-slots', SittingPlan.get_slots, name='get_slots'),
    path('echallan', ChallanController.entryTestChallan, name='echallan'),
    path('verify_echallan', ChallanController.verifyEntryTestChallan, name='verify_echallan'),
    path('entrytest-challan-rejection-reason', CandidateController.rejection_reason, name='entrytest_challan_rejection_reason'),
    path('entrytestresult', EntryTestController.result, name='entrytestresult'),
    path('markresult', EntryTestController.uploadResult, name='markresult'),

    #merit lists

    path('meritlist/bachelor',MeritListController.meritlists_bachelor,name='meritlists_bachelor'),
    path('meritlist/mphill',MeritListController.meritlists_mphill,name='meritlists_mphill'),
    path('meritlist/phd', MeritListController.meritlists_phd, name='meritlists_phd'),

    path('calculator',MeritListController.calculator,name='calculator'),
    # admissions
    path('admission_challan', ChallanController.admissionChallan, name='admission_challan'),
    path('verify_adchallan', ChallanController.verifyAdmissionChallan, name='verify_adchallan'),
    path('admission-challan-rejection-reason', CandidateController.rejection_reason, name='admission_challan_rejection_reason'),
    path('qualification', QualificationController.index, name='qualification'),
    path('verify_qualification', QualificationController.verifyQualification, name='verify_qualification'),
]
