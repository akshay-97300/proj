from django.db import models


# Create your models here.

class Company(models.Model):
    company = models.CharField(max_length=30)
    address = models.CharField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=30)


class Task(models.Model):
    task = models.CharField(max_length=100)
    is_comleted = models.BooleanField(default=False)
