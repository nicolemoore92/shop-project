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

    def total_cost(order):
        """Calculate the total cost of the order from cost and quantity"""
        total = (float(order.cost) * order.qty)
        print(f"Your total cost is: £{total}")

def display_products(products):
    print("Name: Cost:")
    for product in products:
        print(f"{product.name.title()} {product.cost}")


def display_product(product):
    print("Name: Cost:")
    print(f"{product.name.title()} {product.cost}")


my_product = Product("alice in wonderland", "10.00", "children's book")
hobbit = Product("the hobbit", "9.99", "fantasy adventure")

books = [my_product, hobbit]

#display_product(my_product)
#display_product(hobbit)
display_products(books)

def take_purchase(product_instance, qty):
    new_order = Order(product_instance.name, product_instance.cost, qty)
    return new_order


first_order = take_purchase(my_product, 2)
print(first_order)

print("The total cost of my first order...")
first_order.total_cost()
