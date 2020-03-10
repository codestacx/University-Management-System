from django.urls import path
from admin.Controllers import AuthController
from admin.Controllers import CandidateController
from admin.Controllers import SittingPlan
from admin.Controllers import ChallanController
urlpatterns = [
    path('',AuthController.index,name='adminlogin'),
    path('home',AuthController.home,name='admin_home'),
    path('signout',AuthController.logout,name='admin_logout'),

    #students delete
    path('remove_student',CandidateController.removeStudent,name="remove_student"),

    #hall
    path('upload_hall',SittingPlan.uploadHall,name="upload_hall"),
    #slots
    path('upload_slot',SittingPlan.uploadSlot,name='upload_slot'),
    #verify entry test challan
    path('echallan',ChallanController.entryTestChallan,name='echallan'),
    path('verify_echallan',ChallanController.verifyEntryTestChallan,name='verify_echallan'),
]