from django.db import models
from candidates.models import Degree, User, DegreeCriteria

class Qualification(models.Model):
    candidate      = models.ForeignKey('User', on_delete=models.CASCADE)
    degree         = models.ForeignKey('Degree', on_delete=models.CASCADE)
    criteria       = models.ForeignKey('DegreeCriteria', on_delete=models.CASCADE)
    total_marks    = models.IntegerField()
    obtained_marks = models.IntegerField()
    institute      = models.CharField(max_length=50)
    passing_year   = models.IntegerField( )

    class Meta:
        app_label = 'candidates'