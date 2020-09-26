from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import CustomUser

# Create your tests here.

class costum_user_test(TestCase):

    # def test_conn(self):
    #     pass

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='Mohammed',
            email='mghafri@gmail.com',
            password='M159753$'
        )
        
    # def setUp(self):
    #     self.email = 'Ghafri@gmail.com'
    #     self.password = 'G123456$'

    def test_signup_page_url_and_template(self):
        response = self.client.get("/new_user/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='registration/signup.html')

    def test_home_page_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)

    def test_signup(self):
        response = self.client.post('/new_user/signup/', data={
            
            'email address': 'Ghafri@gmail.com',
            'password': 'G123456$',
        })
        self.assertEqual(response.status_code, 200)
       
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
      

 