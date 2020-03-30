from unittest import TestCase
from products import Product
import json
from decimal import Decimal
from save_products_to_json import save_products_to_json
from textwrap import dedent

class SaveProductsToJson(TestCase):
    def test_save_products_to_json(self):
        product1 = Product("alice in wonderland", Decimal("10.00"), "children's book")
        product2 = Product("the hobbit", Decimal("9.99"), "fantasy adventure")
        product_list = [product1, product2]

        save_products_to_json(product_list)

        expected_data = dedent("""\
        [
         {
          "name": "alice in wonderland",
          "cost": "10.00",
          "description": "children's book"
         },
         {
          "name": "the hobbit",
          "cost": "9.99",
          "description": "fantasy adventure"
         }
        ]
        """).rstrip()

        with open("product_data.json") as pdata:
            self.assertEqual(pdata.read(), expected_data)
