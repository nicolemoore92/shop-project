from products import Product

def display_products(products):
    """Display many products function"""
    d_products = ["Name: Cost: "]
    for product in products:
        d_products.append(f"\n {product.name.title()} £{product.cost}")
    return "".join(d_products)
