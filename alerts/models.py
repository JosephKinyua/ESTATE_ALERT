from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()


