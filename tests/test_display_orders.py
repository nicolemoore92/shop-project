from unittest import TestCase
from orders import Order
from decimal import Decimal
from display_orders import display_orders
from textwrap import dedent

class TestDisplayOrders(TestCase):
    def test_display_orders(self):
        order = Order("the hobbit", Decimal("9.99"), 3)
        order_list = [order]
        display = display_orders(order_list)
        expected_display = dedent("""\
            Product Name: Cost: Quantity:
            The Hobbit £9.99 3
            Your total cost is: £29.97
            """).rstrip()

        self.assertEqual(1,1)

        print(display_orders(order_list))
