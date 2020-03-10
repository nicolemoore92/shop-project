from unittest import TestCase
from decimal import Decimal
from take_purchase import take_purchase
from products import Product

class TakePurchase(TestCase):
    def test_take_purchase(self):
        product = Product("alice in wonderland", Decimal("10.00"), "children's book")
        purchase = take_purchase(product, 2)
        self.assertEqual(purchase.product_name, "alice in wonderland")
        self.assertEqual(purchase.cost, Decimal("10.00"))
        self.assertEqual(purchase.qty, 2)
