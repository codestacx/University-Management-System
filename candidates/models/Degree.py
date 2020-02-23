from django.db import models
from datetime import date
from candidates.models.User import User

# degree model

class Degree(models.Model):
    degree_id = models.AutoField(primary_key = True)
    degree_name = models.CharField('degree_name',max_length=50)
    degree_level = models.CharField('degree_level',max_length=50)


    class Meta:
        app_label = 'candidates'


class DegreeCriteria(models.Model):
    degree_criteria_id = models.AutoField(primary_key = True)
    degree = models.ForeignKey(Degree,on_delete=models.CASCADE)
    requirement = models.CharField(max_length=50)

    class Meta:
        app_label = 'candidates'

class DegreeOffering(models.Model):
    degree_offering_id = models.AutoField(primary_key = True)
    session = models.IntegerField(null=False)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)

    class Meta:
        app_label = 'candidates'

class Qualification(models.Model):

    candidate = models.ForeignKey(User,on_delete=models.CASCADE)
    degree   = models.ForeignKey(Degree,on_delete=models.CASCADE)
    criteria = models.ForeignKey(DegreeCriteria,on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    obtained_marks = models.IntegerField()
    institute = models.CharField(max_length=50)
    passing_year = models.IntegerField( )

    class Meta:
        app_label = 'candidates'
