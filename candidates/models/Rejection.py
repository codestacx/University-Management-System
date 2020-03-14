from django.db import models
from django.utils import timezone as tz


class Rejection(models.Model):
    candidate_id = models.IntegerField(primary_key=True)
    reason = models.CharField('reason', max_length=100, blank=False)
    category = models.CharField('category', max_length=10, blank=False)

    def __str__(self):
        return f"{self.reason} for candidate id: {self.candidate_id}"
