from orders import Order
from decimal import Decimal
from products import Product

def take_purchase(product_instance, qty):
    """Take a purchase"""
    new_order = Order(product_instance.name, product_instance.cost, qty)
    return new_order
