from products import Product

def display_products(products):
    """Display many products function"""
    print("Name: Cost:")
    for product in products:
        print(f"{product.name.title()} £{product.cost}")
