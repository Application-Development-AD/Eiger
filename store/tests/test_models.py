#to test model

from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product


class TestCategoriesModel(TestCase):

    #for 1 simple test
    def setUp(self):
        self.data1 = Category.objects.create(name='New Arrival', slug='new-arrival')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        #use assertTrue
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """
        Test Category model default name
        """
        data = self.data1
        #use assertEqual
        self.assertEqual(str(data), 'New Arrival')

class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='New Arrival', slug='new-arrival')
        User.objects.create(username='eiger')
        self.data1 = Product.objects.create(category_id=1, title='Panduan Umum Keselamatan Makmal dan Bengkel Universiti', created_by_id=1, 
                                            slug='	panduan-umum-keselamatan-makmal-dan-bengkel-universiti', price='50.00', image='pansafe')
    
    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data),'Panduan Umum Keselamatan Makmal dan Bengkel Universiti')
