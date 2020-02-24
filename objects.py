class Product():
    """Defining a product"""
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    def __str__(self):
        #returns nice printable version of the object
        return self.name


class Order():
    """Defining an order"""
    def __init__(self, product_name, cost, qty):
        self.product_name = product_name
        self.cost = cost
        self.qty = qty

    def __str__(self):
        return f"Order: {self.qty} of {self.product_name}."

def display_products(products):
    print("Name: Cost:")
    for product in products:
        print(product.name.title() + " " + product.cost)


def display_product(product):
    print("Name: Cost:")
    print(product.name.title() + " " + product.cost)


my_product = Product("alice in wonderland", "£10.00", "children's book")
hobbit = Product("the hobbit", "£9.99", "fantasy adventure")

books = [my_product, hobbit]

#display_product(my_product)
#display_product(hobbit)
display_products(books)

def take_purchase(product, qty):
    new_order = Order(product.name, qty)



first_order = take_purchase(my_product, 2)
print(first_order)
