from unittest import TestCase
from products import Product
from decimal import Decimal
from display_product import display_product

class TestDisplayProduct(TestCase):
    def test_display_product(self):
        product = Product("alice in wonderland", Decimal("10.00"), "children's book")
        display = display_product(product)
        expected_display = "Name: Cost: \nAlice In Wonderland £10.00"
        self.assertEqual(display, expected_display)
