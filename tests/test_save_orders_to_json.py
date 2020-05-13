from unittest import TestCase
from save_orders_to_json import dump_orders_to_json
from products import Product
from orders import Order
from decimal import Decimal
import json


class TestDumpOrdersToJson(TestCase):
    def test_dump_order_to_json(self):
        order1 = Order("the hobbit", Decimal("9.99"), 3)
        order2 = Order("alice in wonderland", Decimal("10.00"), 2)
        orders_list = [order1, order2]

        output = dump_orders_to_json(orders_list)

        expected_output = [
             {
              "product name": "the hobbit",
              "cost": "9.99",
              "quantity": 3
             },
             {
              "product name": "alice in wonderland",
              "cost": "10.00",
              "quantity": 2
             }
            ]
        self.assertEqual(json.loads(output), expected_output)
