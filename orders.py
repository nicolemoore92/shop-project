class Order():
    """Defining an order"""
    def __init__(self, product_name, cost, qty):
        self.product_name = product_name
        self.cost = cost
        self.qty = qty

    def __str__(self):
        return f"Order: {self.qty} of {self.product_name}."

    def total_cost(self):
        """Calculate the total cost of the order from cost and quantity"""
        return self.cost * self.qty
