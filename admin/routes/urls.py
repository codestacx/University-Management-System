from django.urls import path
from admin.Controllers import AuthController
from admin.Controllers import CandidateController
from admin.Controllers import SittingPlan
from admin.Controllers import ChallanController
from admin.Controllers import EntryTestController
from admin.Controllers import QualificationController
urlpatterns = [
    path('',AuthController.index,name='adminlogin'),
    path('home',AuthController.home,name='admin_home'),
    path('signout',AuthController.logout,name='admin_logout'),

    #students delete
    path('remove_student',CandidateController.removeStudent,name="remove_student"),

    #hall
    path('upload_hall',SittingPlan.uploadHall,name="upload_hall"),
    path('get-halls', SittingPlan.get_halls, name='get_halls'),

    #slots
    path('upload_slot',SittingPlan.uploadSlot,name='upload_slot'),
    path('get-slots', SittingPlan.get_slots, name='get_slots'),
    
    #verify entry test challan
    path('echallan',ChallanController.entryTestChallan,name='echallan'),
    path('verify_echallan',ChallanController.verifyEntryTestChallan,name='verify_echallan'),
    path('entrytest-challan-rejection-reason', ChallanController.entrytest_challan_rejection_reason, name='entrytest_challan_rejection_reason'),
    
    #entry test result
    path('entrytestresult',EntryTestController.result,name='entrytestresult'),
    path('markresult',EntryTestController.uploadResult,name='markresult'),
    #admission challan
    path('admission_challan',ChallanController.admissionChallan,name='admission_challan'),
    path('verify_adchallan', ChallanController.verifyAdmissionChallan, name='verify_adchallan'),
    #qualification
    path('qualification',QualificationController.index,name='qualification'),
    path('verify_qualification', QualificationController.verifyQualification, name='verify_qualification'),
]