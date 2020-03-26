from products import Product
from decimal import Decimal

def display_product(product):
    """Display a product function"""
    return f"Name: Cost: \n{product.name.title()} £{product.cost}"

product = Product("alice in wonderland", Decimal("10.00"), "children's book")

print(display_product(product))
