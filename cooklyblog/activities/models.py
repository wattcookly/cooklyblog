from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.


class Activity(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    location = PlainLocationField(zoom=7)

    def __str__(self):
        return self.title


class Session(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    session_name = models.CharField(max_length=120)
    activity = models.ForeignKey(Activity)

    def __str__(self):
        return self.title
