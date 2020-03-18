from django.db import models
from candidates.models.User import User
from candidates.models.Degree import Degree
from datetime import date
from candidates.models.User import User
#model that hold the information -> applied candidate & degree in which he/she applied
class AppliedCandidate(models.Model):
    candidate = models.ForeignKey('User', on_delete=models.CASCADE)
    degree = models.ForeignKey('Degree', null=True, on_delete=models.CASCADE)
    paid_challan_copy = models.ImageField('Image', upload_to='candidates/uploads/paid_challans')
    challan_status = models.IntegerField(default=0)

    class Meta:
        app_label = 'candidates'




#model contains meta data of tests

class TestTypes(models.Model):
    test_id = models.AutoField(primary_key=True)
    degree = models.ForeignKey(Degree,on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    conducted_date = models.DateField(default=date.today)
    class Meta:
        app_label = 'candidates'

#model that contain the results of entry test

class EntryTestResult(models.Model):
    candidate = models.ForeignKey(User,on_delete=models.CASCADE)
    test = models.ForeignKey(TestTypes,on_delete=models.CASCADE)
    obtained_marks = models.IntegerField()

    class Meta:
        app_label = 'candidates'



