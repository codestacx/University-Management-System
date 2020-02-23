from django.db import models
from candidates.models import Degree

class DegreeCriteria(models.Model):
    degree_criteria_id = models.AutoField(primary_key=True)
    requirement        = models.CharField(max_length=50)
    degree             = models.ForeignKey('Degree', on_delete=models.CASCADE)

    class Meta:
        app_label = 'candidates'