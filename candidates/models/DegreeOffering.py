from django.db import models
from datetime import date

class DegreeOffering(models.Model):
    degree_offering_id = models.AutoField(primary_key=True)
    session            = models.IntegerField(null=False)
    start_date         = models.DateField(default=date.today)
    end_date           = models.DateField(default=date.today)

    class Meta:
        app_label = 'candidates'