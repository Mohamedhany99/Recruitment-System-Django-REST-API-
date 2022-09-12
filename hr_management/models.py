from django.db import models

# Create your models here.
class Employee(models.Model):
    

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    salary = models.FloatField()
    hired_date = models.DateTimeField(blank=True, null=True, default=None)
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='Employee')