from django.test import TestCase
from .models import Image,category,Location

class ImageTestClass(TestCase):
    def setUp(self):
        self.dog = Image(name = 'dog',)

# Create your tests here.
