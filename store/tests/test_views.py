#to test view

from unittest import skip
from django.http.request import HttpRequest

from django.test import TestCase 

from django.contrib.auth.models import User
from django.urls import reverse
from store.models import Category, Product
from django.test import Client

from store.views import all_products

#simple skip test
#@skip("demonstrating skipping")
#class TestSkip(TestCase):
#    def test_skip_example(self):
#        pass

#to test client 
#def test_homepage_url(self):
 #   """
  #  Test homepage response status
   # """
    #response = self.Client.get('/')

#to test client
class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='eiger')
        Category.objects.create(name='New Arrival',slug='new-arrival')
        Product.objects.create(category_id=1, title='Panduan Umum Keselamatan Makmal dan Bengkel Universiti', created_by_id=1, 
                                slug='	panduan-umum-keselamatan-makmal-dan-bengkel-universiti', price='50.00', image='pansafe')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    #to test reverse
    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['panduan-umum-keselamatan-makmal-dan-bengkel-universiti']))
        self.assertEqual(response.status_code, 200)

    #to test category detail
    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store:category_list', args=['new-arrival']))
        self.assertEqual(response.status_code, 200)

    #to test homepge
    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        print(html)
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
    
