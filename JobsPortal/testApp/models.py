from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    mail=models.EmailField()
    mobile=models.IntegerField()

class bangjobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    mail=models.EmailField()
    mobile=models.IntegerField()

class chennaijobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    mail=models.EmailField()
    mobile=models.IntegerField()

class punejobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    eligibility=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    mail=models.EmailField()
    mobile=models.IntegerField()
