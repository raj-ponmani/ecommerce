import random
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from products.models import Products


# helper function
def create_random_products(num_products):
    products_list = []
    for i in range(num_products):
        product = Products.objects.create(name=f"product{random.randint(100, 1000)}",
                                          description=f"test description{random.randint(2015, 2019)}",
                                          price=random.randint(100, 1000))
        products_list.append(product)
    return products_list


class ProductAPIViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        num_product = 10
        self.product_list = create_random_products(num_product)

    def test_product_list(self):
        url = reverse('products:product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        product_expected_list = self.product_list
        product_result_list = response.data
        self.assertEqual(len(product_result_list), len(product_expected_list))

        for i in range(len(product_expected_list)):
            student_exp = product_expected_list[i]
            student_res = product_expected_list[i]

            self.assertEqual(student_exp.name, student_res.name)
            self.assertEqual(student_exp.description, student_res.description)
            self.assertEqual(student_exp.price, student_res.price)
