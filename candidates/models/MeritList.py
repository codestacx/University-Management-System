from django.db import models
from candidates.models.User import User
from candidates.models.PriorityDegree import *

class MeritList(models.Model):
    candidate = models.ForeignKey(User,on_delete=models.CASCADE)
    selection_status = models.IntegerField(default=0)
    class Meta:
        app_label='candidates'

class Agreegat(models.Model):
    total = models.CharField(max_length=100)
    candidate = models.ForeignKey(User,on_delete=models.CASCADE)

class SelectedMeritPrograms(models.Model):
    meritlist = models.ForeignKey(MeritList,on_delete=models.CASCADE)
    selected_program = models.ForeignKey(PrioriyDegree,on_delete=models.CASCADE)
    program_status = models.IntegerField(default=0)
    class Meta:
        app_label = 'candidates'

