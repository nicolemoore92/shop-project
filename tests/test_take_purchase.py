from unittest import TestCase
from decimal import Decimal
from take_purchase import take_purchase
from products import Product

class TakePurchase(TestCase):
    def test_take_purchase(self):
        product = Product("alice in wonderland", Decimal("10.00"), "children's book")
        quantity = 2

        purchase = take_purchase(product, quantity)

        self.assertEqual(purchase.product_name, product.name)
        self.assertEqual(purchase.cost, product.cost)
        self.assertEqual(purchase.qty, quantity)
