from decimal import Decimal
from products import Product
from orders import Order
from take_purchase import take_purchase
from display_products import display_products
from display_product import display_product
from display_order import display_order
from display_orders import display_orders
from save_products_to_json import dump_products_to_json
from save_orders_to_json import dump_orders_to_json
import json

if __name__ == '__main__':

    my_product = Product("alice in wonderland", Decimal("10.00"), "children's book")
    hobbit = Product("the hobbit", Decimal("9.99"), "fantasy adventure")
    books = [my_product, hobbit]
    products = [my_product, hobbit]

    output = dump_products_to_json(products)
    filename = 'product_data.json'
    with open(filename, 'w') as pd:
        pd.write(output)

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
    print(display_products(loaded_products))

    print(display_product(my_product))
    print(display_product(hobbit))

    print(display_products(books))

if __name__ == "__main__":

    first_order = take_purchase(my_product, 2)
    print(first_order)

    print("The total cost of my first order...")
    first_order.total_cost()

    #my_order = Order(f"{my_product.name.title()}", f"{my_product.cost}", "2")

    print("\nMy first order:\n")
    print(display_order(first_order))

    my_order = Order("the hobbit", Decimal("9.99"), 3)
    another_order = Order("alice in wonderland", Decimal("10.00"), 2)
    orders_list = [my_order, another_order]
    orders2 = [my_order, another_order, first_order]

    order_output = dump_orders_to_json(orders2)
    filename = 'order_data.json'
    with open(filename, 'w') as od:
        od.write(order_output)


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
    print(display_orders(loaded_orders))

    print(display_order(my_order))
    print(display_order(another_order))

    print(display_orders(orders_list))

    print("\nTotal:\n")
    print(f"£{my_order.total_cost()}")
    print(f"£{another_order.total_cost()}")
