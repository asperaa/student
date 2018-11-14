from django.db import models
from django.conf import settings

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name