from unittest import TestCase
from orders import Order
from decimal import Decimal


class TestOrders(TestCase):
    def test_order(self):
        order = Order('alice in wonderland', Decimal("10.00"), 2)
        self.assertEqual(order.product_name,'alice in wonderland')
        self.assertEqual(order.cost, Decimal("10.00"))
        self.assertEqual(order.qty, 2)

    def test_str(self):
        order1 = Order('alice in wonderland', Decimal("10.00"), 2)
        self.assertEqual(str(order1),"Order: 2 of alice in wonderland.")

    def test_total_cost(self):
        order = Order('alice in wonderland', Decimal("10.00"), 2)
        self.assertEqual(order.total_cost(), Decimal("20.00"))
