from unittest import TestCase
from display_products import display_products
from products import Product

class TestDisplayProducts(TestCase):
    def test_display_products(self):
        product = Product('alice in wonderland', Decimal("10.00"), 'childrens book')
        self.assertEqual(1,1)
