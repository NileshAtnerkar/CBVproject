from django.db import models
from django import forms

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    salary=models.IntegerField()
    company=models.CharField(max_length=30)

    def __str__(s):
        return s.name

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields="__all__"

    

class Product(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    pirce=models.IntegerField()
     

