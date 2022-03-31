from django.test import TestCase
from django.test import Client
from ..models import *



class IntegracaoComAPINode(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Usuario.objects.create(username='Klinsman', password='12345678',
                               matricula='0022', email='test@example.com'
                               )
        print('User created!')