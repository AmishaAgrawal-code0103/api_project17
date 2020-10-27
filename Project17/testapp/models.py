from django.db import models

# Create your models here.
class Student(models.Model):
	sname = models.CharField(max_length=50)
	semail = models.EmailField()
	sphone_no = models.IntegerField()
	saddress = models.CharField(max_length=50)
