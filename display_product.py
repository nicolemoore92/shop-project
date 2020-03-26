from products import Product

def display_product(product):
    """Display a product function"""
    return f"Name: Cost: \n{product.name.title()} £{product.cost}"
