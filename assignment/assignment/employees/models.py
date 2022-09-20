from django.db import models
from users.models import User
from departments.models import Department, Task, Company


# Create your models here.

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager')
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    salary = models.FloatField(max_length=20)



