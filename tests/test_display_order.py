from unittest import TestCase
from orders import Order
from decimal import Decimal
from display_order import display_order
from textwrap import dedent

class TestDisplayOrder(TestCase):
    def test_display_order(self):
        order = Order("the hobbit", Decimal("9.99"), 3)
        d_order = display_order(order)
        expected_display = dedent("""\
            Product Name: Cost: Quantity:
            The Hobbit £9.99 3
            Your total cost is: £29.97
            """).rstrip()
        self.assertEqual(d_order,expected_display)
