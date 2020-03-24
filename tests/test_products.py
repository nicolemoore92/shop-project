from unittest import TestCase
from products import Product
from decimal import Decimal

class TestProducts(TestCase):
    def test_product(self):
        product = Product('alice in wonderland', Decimal("10.00"), 'childrens book')
        self.assertEqual(product.name,'alice in wonderland')
        self.assertEqual(product.cost, Decimal("10.00"))
        self.assertEqual(product.description, 'childrens book')

    def test_str(self):
        product = Product('alice in wonderland', Decimal("10.00"), 'childrens book')
        self.assertEqual(str(product.name), 'alice in wonderland')
