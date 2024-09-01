from typing import Self
from django.db import models

# Create your models here.
class Employee(models.Model):
  
  name=models.CharField(max_length=25,blank=False,null=False)
  email=models.EmailField()
  age=models.IntegerField()
  gender=models.CharField(max_length=25,blank=False,null=False)

  
def __str__(self):
        return f'{self.first_name} {self.last_name}'

  