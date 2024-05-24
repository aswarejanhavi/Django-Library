from django.db import models


# Create your models here.

class Book(models.Model):
    Title=models.CharField(max_length=250)
    Author=models.CharField(max_length=250)
    ISBN=models.IntegerField()
    Publication_date=models.DateField()
    Availability=models.CharField("Avaliabile_Book YES /NO",max_length=25)

class Borrower(models.Model):
    Name=models.CharField(max_length=250)
    Email=models.CharField(max_length=200)
    borrower_Book=models.CharField("Borrower YES/NO",max_length=25)

