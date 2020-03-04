from decimal import Decimal
from products import Product
from orders import Order
import json

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

def save_products_to_json(products, filename = 'product_data.json'):
    product_dicts = []
    for product in products:
        product_dict = {'name': product.name, 'cost': str(product.cost), 'description': product.description}
        product_dicts.append(product_dict)
    with open(filename, 'w') as pd:
        json.dump(product_dicts,pd, indent=1)

save_products_to_json(books)

def load_products_from_json(filename = 'product_data.json'):
    with open(filename) as pdf:
        products_from_file = json.load(pdf)
    print(f"PRODUCTS {products_from_file}")
    product_list = []
    for product_dict in products_from_file:
        product = Product(product_dict['name'], Decimal(product_dict['cost']), product_dict['description'])
        product_list.append(product)
    return product_list

loaded_products = load_products_from_json()
print("HERE ARE THE PRODUCTS")
display_products(loaded_products)

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
orders_list = [my_order, another_order, first_order]

def save_orders_to_json(orders, filename = 'order_data.json'):
    order_dicts = []
    for order in orders:
        order_dict = {'product name': order.product_name, 'cost': str(order.cost), 'quantity': order.qty}
        order_dicts.append(order_dict)
    with open(filename, 'w') as od:
        json.dump(order_dicts, od, indent=1)

save_orders_to_json(orders_list)

def load_orders_from_json(filename = 'order_data.json'):
    with open(filename) as odf:
        orders_from_file = json.load(odf)
        order_list = []
        for order_dict in orders_from_file:
            order = Order(order_dict['product name'],Decimal(order_dict['cost']),order_dict['quantity'])
            order_list.append(order)
        return order_list

loaded_orders = load_orders_from_json()
print("MY NEW ORDERS")
display_orders(loaded_orders)

display_order(my_order)
display_order(another_order)

display_orders(orders_list)

print("\nTotal:\n")
print(f"£{my_order.total_cost()}")
print(f"£{another_order.total_cost()}")
