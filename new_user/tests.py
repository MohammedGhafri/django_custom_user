from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser

# Create your tests here.

class costum_user_test(TestCase):

    def test_conn(self):
        pass

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Mohammed',
            email='mghafri@gmail.com',
            password='M159753$'
        )
        