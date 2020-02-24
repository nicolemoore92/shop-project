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
