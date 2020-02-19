from django.db import models


class Degree(models.Model):
    #degree_id    = models.AutoField(primary_key=True)
    degree_name  = models.CharField('degree_name', max_length=50)
    degree_level = models.CharField('degree_level', max_length=50)


    # class Meta:
    #     app_label = 'candidates'
