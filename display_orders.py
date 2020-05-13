from orders import Order
from textwrap import dedent

def display_orders(orders):
    """display many orders function"""
    disp_orders = ["Product Name: Cost: Quantity:"]

    for order in orders:
        total = order.total_cost()
        disp_orders.append(dedent(f"""\
            {order.product_name.title()} £{order.cost} {order.qty}
            Your total cost is: £{total}
            """).rstrip())
        return "\n".join(disp_orders)
