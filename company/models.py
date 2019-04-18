from django.db import models
# import MySQLdb

# Create your models here.

class Company(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=250)


    def __str__(self):
        return  self.name

    class Meta:
        db_table ='company'


class TestModel(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.name