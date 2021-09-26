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



class TestNeighborhood(TestCase):
    def setUp(self):
        self.location = Location.objects.create(location='Machakos')
        self.hood = Neighborhood.objects.create(name='Kisumu Ndogo', location=self.location, policehelpline=2, hospitalhelpline=2, occupants=8)


    def tearDown(self):
        Location.objects.all().delete()
        Neighborhood.objects.all().delete()

    def test_isinstance(self):
        self.assertTrue(isinstance(self.hood, Neighborhood))


    def test_updateneighbor(self):
        self.hood2 = Neighborhood.objects.create(name='Embakasi', location=self.location, policehelpline= 2, hospitalhelpline=4, occupants=8)
        Neighborhood.update_neighborhood(self.hood2.id, name='kajiado')
        updated = Neighborhood.objects.get(id = self.hood2.id)
        self.assertEqual(updated.name, 'kajiado')