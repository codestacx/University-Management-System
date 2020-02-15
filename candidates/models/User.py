from django.db import models
from django.utils import timezone as tz


class User(models.Model):
    email      =  models.EmailField('email',max_length=40,unique=True)
    password   =  models.CharField('password',null=False,max_length=255)
    role       =  models.CharField('role',max_length=20)
    created_at = models.DateField(default=tz.now)
    updated_at = models.DateField(default=tz.now)
    class Meta:
        app_label = 'candidates'

    def __str__(self):
        return f"email: {self.email} "