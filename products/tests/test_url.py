from django.urls import resolve
from rest_framework.reverse import reverse
from rest_framework.test import APISimpleTestCase
from products.views import ProductView


class TestUrls(APISimpleTestCase):
    def setUp(self):
        self.base_url = '/'
        self.app_name = 'products'
        return

    def test_product_list_url(self):
        url = reverse('products:product')
        resolved = resolve(url)
        self.assertEqual(resolved.func.__name__, ProductView.as_view().__name__)
        self.assertEqual(resolved.namespace, self.app_name)
        self.assertEqual(url, f'{self.base_url}api/product-list/')