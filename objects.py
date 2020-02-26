#define Product class
class Product():
    """Defining a product"""
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    def __str__(self):
        #returns nice printable version of the object
        return self.name

#define Order class
class Order():
    """Defining an order"""
    def __init__(self, product_name, cost, qty):
        self.product_name = product_name
        self.cost = cost
        self.qty = qty

    def __str__(self):
        return f"Order: {self.qty} of {self.product_name}."

#display many products function
def display_products(products):
    print("Name: Cost:")
    for product in products:
        print(product.name.title() + " " + product.cost)

#display a product function
def display_product(product):
    print("Name: Cost:")
    print(product.name.title() + " " + product.cost)


my_product = Product("alice in wonderland", "£10.00", "children's book")
hobbit = Product("the hobbit", "£9.99", "fantasy adventure")

books = [my_product, hobbit]

#display_product(my_product)
#display_product(hobbit)
print("Here are the books!!!")
display_products(books)

#take a purchase function
def take_purchase(product_instance, qty):
    new_order = Order(product_instance.name, product_instance.cost, qty)
    return new_order

first_order = take_purchase(my_product, 2)
print(first_order)

#display an order function
def display_order(order):
    print("Product Name: Cost: Quantity:")
    print(f"{order.product_name.title()} {order.cost} {order.qty}")

#my_order = Order(f"{my_product.name.title()}", f"{my_product.cost}", "2")

#display many orders function
def display_orders(orders):
    print("Product Name: Cost: Quantity:")
    for order in orders:
        print(order.product_name.title() + " " + order.cost + " " + order.qty)

my_order = Order("the hobbit", "£9.99", "3")
another_order = Order("alice in wonderland", "£10.00", "2")

orders_list = [my_order, another_order]

display_order(my_order)
display_order(another_order)


display_orders(orders_list)
