from decimal import Decimal
from products import Product
from orders import Order

def display_products(products):
    """Display many products function"""
    print("Name: Cost:")
    for product in products:
        print(f"{product.name.title()} £{product.cost}")

def display_product(product):
    """Display a product function"""
    print("Name: Cost:")
    print(f"{product.name.title()} £{product.cost}")


my_product = Product("alice in wonderland", Decimal("10.00"), "children's book")
hobbit = Product("the hobbit", Decimal("9.99"), "fantasy adventure")

books = [my_product, hobbit]

display_product(my_product)
display_product(hobbit)

display_products(books)

def take_purchase(product_instance, qty):
    """Take a purchase"""
    new_order = Order(product_instance.name, product_instance.cost, qty)
    return new_order

first_order = take_purchase(my_product, 2)
print(first_order)

print("The total cost of my first order...")
first_order.total_cost()

def display_order(order):
    """display an order function"""
    print("Product Name: Cost: Quantity:")
    print(f"{order.product_name.title()} £{order.cost} {order.qty}")
    total = order.total_cost()
    print(f"Your total cost is: £{total}")

#my_order = Order(f"{my_product.name.title()}", f"{my_product.cost}", "2")

print("\nMy first order:\n")
display_order(first_order)

def display_orders(orders):
    """display many orders function"""
    print("Product Name: Cost: Quantity:")
    for order in orders:
        print(f"{order.product_name.title()} £{order.cost} {order.qty}")
        total = order.total_cost()
        print(f"Your total cost is: £{total}")

my_order = Order("the hobbit", Decimal("9.99"), 3)
another_order = Order("alice in wonderland", Decimal("10.00"), 2)

orders_list = [my_order, another_order]

display_order(my_order)
display_order(another_order)

display_orders(orders_list)

print("\nTotal:\n")
print(f"£{my_order.total_cost()}")
print(f"£{another_order.total_cost()}")
