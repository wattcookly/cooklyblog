from django.db import models

# Create your models here.


class Transaction(models.Model):
    date = models.DateField()
    seat = models.IntegerField()
