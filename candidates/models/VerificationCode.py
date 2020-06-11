from django.db import models
from django.utils import timezone as tz


def calc_expires_at():
    return tz.now() + tz.timedelta(days=1)

class VerificationCode(models.Model):
    code       = models.IntegerField('code', blank=False )
    email      = models.EmailField('email', blank=False, max_length=40)
    expires_at = models.DateTimeField('expires_at', blank=False, default=calc_expires_at)
    status     = models.IntegerField('status', default=0)
    def __str__(self):
        return f"{self.code} for {self.email}"
