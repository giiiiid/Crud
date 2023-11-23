from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def req(self):
        self.client = Client()
        # self.index = reverse('index')

    def test_index(self):
        response = self.client.get(reverse('index'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_user_home(self):
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-home.html')
        
