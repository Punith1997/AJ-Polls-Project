from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class pollsmodel(models.Model):
    uname=models.CharField(max_length=30,default=None)
    game=models.CharField(max_length=30,default=None)
    vote=models.IntegerField(default=0)

    class Meta:
        ordering=("uname",)

class totalpolls(pollsmodel):
    class Meta:
        proxy=True
