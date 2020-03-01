from django.db import models
from django.utils import timezone as tz


class WizardSession(models.Model):
    user_id = models.IntegerField(primary_key=True)
    data = models.TextField('data')

    def __str__(self):
        return f"{self.user_id} for {self.data}"
