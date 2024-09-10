from django.test import TestCase
from .models import Product

class MainTest(TestCase):

    def setUp(self):
        self.client = self.client

    def test_main_url_is_exist(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = self.client.get('/Arisha/')
        self.assertEqual(response.status_code, 404)

    def test_create_product_entry(self):
        product = Product.objects.create(
            name="Test Product",
            price=100,
            description="This is a test product."
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.description, "This is a test product.")

    def test_product_entry_can_be_saved_and_retrieved(self):
        product = Product.objects.create(
            name="Another Test Product",
            price=200,
            description="This is another test product."
        )
        saved_product = Product.objects.get(id=product.id)
        self.assertEqual(saved_product.name, "Another Test Product")
        self.assertEqual(saved_product.price, 200)
        self.assertEqual(saved_product.description, "This is another test product.")

