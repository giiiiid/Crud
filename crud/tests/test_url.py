from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import index, user_home, detail, update, done, delete, search, sign_up, login_user, logout_user


class TestUrls(SimpleTestCase):

    def test_index_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
    
    def test_user_home_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, user_home)
    
    def test_detail_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)
    
    def test_signup_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, sign_up)
    
    def test_login_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login_user)
    
    def test_logout_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_user)
    
    # def test_detail_resolved(self):
    #     w = self
    #     url = reverse('detail', kwargs={'activity':w.activity})
    #     self.assertEquals(resolve(url).func, detail)