from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
            return self.name

    def create_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def find_neighborhood(cls, searchterm):
        searchresults = cls.objects.filter(Q(name__icontains=searchterm))
        return searchresults

    @classmethod
    def update_neighborhood(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

class Profile(models.Model):