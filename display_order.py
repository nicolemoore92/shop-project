from orders import Order
from textwrap import dedent

def display_order(order):
    """display an order function"""
    total = order.total_cost()
    return dedent(f"""\
        Product Name: Cost: Quantity:
        {order.product_name.title()} £{order.cost} {order.qty}
        Your total cost is: £{total}
        """).rstrip()
