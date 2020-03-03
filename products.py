class Product():
    """Defining a product"""
    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description

    def __str__(self):
        """Returns nice printable version of the object"""
        return self.name
