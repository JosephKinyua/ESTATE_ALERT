from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
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
    policehelpline = models.IntegerField(null=True, blank=True)
    hospitalhelpline = models.IntegerField(null=True, blank=True)
    occupants = models.IntegerField(default=0, null=True)


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
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField()
    phone = models.IntegerField(null=True, blank=True)
    profilePic = models.ImageField(upload_to='userProfile/', default='userProfile/test.png')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(username=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


    def __str__(self):
        return self.username

class Business(models.Model):
    businessname = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, blank=True)
    description = models.TextField()
    email = models.EmailField(max_length=200)
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.businessname

    def save_business(self):
        self.save()

    @classmethod
    def delete_business(cls, id): 
        cls.objects.filter(id=id).delete()

    @classmethod
    def searchbusiness(cls, searchterm):
        searchresults = cls.objects.filter(Q(businessname__icontains = searchterm))
        return searchresults
class Post(models.Model):
    posttitle = models.CharField(max_length=200, null=False, blank=False)
    story = models.TextField()
    timeuploaded = models.DateTimeField(auto_now_add=True)
    postuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.posttitle

    def save_post(self):
        self.save()

    @classmethod
    def delete_post(cls, id):
        cls.objects.filter(id=id).delete()