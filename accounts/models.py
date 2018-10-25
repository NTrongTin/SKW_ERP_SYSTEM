from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    code = models.CharField(max_length=10, unique=True)
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
	
    def __str__(self):
        return self.first_name + " " + self.middle_name + " " + self.last_name
