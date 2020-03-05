from django.db import models
from candidates.models.User import User

class PrioriyDegree(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'candidates'

class DegreePriorities(models.Model):
    priority_id = models.AutoField(primary_key=True)
    candidate = models.ForeignKey(User,on_delete=models.CASCADE)
    priority_a = models.CharField(max_length=50,null=True)
    priority_b = models.CharField(max_length=50,null=True)
    priority_c = models.CharField(max_length=50,null=True)
    priority_d = models.CharField(max_length=50,null=True)
    priority_e = models.CharField(max_length=50,null=True)
    priority_f = models.CharField(max_length=50,null=True)
    priority_g = models.CharField(max_length=50,null=True)
    priority_h = models.CharField(max_length=50,null=True)
    priority_i = models.CharField(max_length=50,null=True)
    priority_j = models.CharField(max_length=50,null=True)
    priority_k = models.CharField(max_length=50,null=True)
    priority_l = models.CharField(max_length=50,null=True)
    priority_form = models.ImageField(upload_to='candidates/uploads/paid_admission_form')
    form_status = models.IntegerField(default=0)
    class Meta:
        app_label = 'candidates'
