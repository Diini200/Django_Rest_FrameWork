from django.db import models
class Employee(models.Model):
    emp_number= models.IntegerField()
    emp_name= models.CharField(max_length =64)
    emp_salary= models.CharField(max_length=64)
    emp_address= models.CharField(max_length=164)
    
