from unittest import TestCase
from display_products import display_products
from products import Product
from decimal import Decimal

class TestDisplayProducts(TestCase):
    def test_display_products(self):
        product = Product('alice in wonderland', Decimal("10.00"), 'childrens book')
        product_list = [product]
        display = display_products(product_list)
        expected_display = "Name: Cost: \n Alice In Wonderland £10.00"

        self.assertEqual(display, expected_display)
