from products import Product
from decimal import Decimal

def display_product(product):
    """Display a product function"""
    return f"Name: Cost: \n{product.name.title()} £{product.cost}"
