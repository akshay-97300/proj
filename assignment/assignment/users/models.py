from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('END_USER', 'EndUser'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    phone_number = models.CharField(unique=True, max_length=20)
    role = models.IntegerField(default='EndUser')
    document = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(['pdf'])])
    created_at = models.DateTimeField(auto_now_add=True)
