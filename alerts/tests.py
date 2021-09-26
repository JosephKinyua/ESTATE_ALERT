from django.test import TestCase
from .models import Business, Location, Profile, Neighborhood, Post
from django.contrib.auth.models import User

class TestLocation(TestCase):
    def setUp(self):
        self.location = Location.objects.create(location='Machakos')

    def tearDown(self):
        Location.objects.all().delete()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location2 = Location.objects.create(location='Nairobi')
        self.assertEqual(len(Location.objects.all()), 2)



