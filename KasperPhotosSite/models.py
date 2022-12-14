from django.db import models
from django.utils import timezone


# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to="gallery/")

class Appointment(models.Model):
    name = models.CharField("Name", max_length=40)
    phoneNumber = models.CharField("Phone Number", max_length=15)
    email = models.EmailField("Email", max_length=80)
    dateRangeLow = models.CharField("Start Date", max_length=30)
    dateRangeHigh = models.CharField("End Date", max_length=30, blank=True)
    location = models.CharField("Address", max_length=200)
    info = models.TextField("Describe Your Photoshoot", max_length=1000)

class Blog(models.Model):
    title = models.CharField("Title", max_length=100)
    createdAt = models.DateTimeField(default=timezone.localtime(timezone.now()))
    blogText = models.TextField("Write Your Blog Post Here")
    image = models.ImageField(null=True, blank=True, upload_to="images/")