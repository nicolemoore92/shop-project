import json

def dump_orders_to_json(orders):
    order_dicts = []
    for order in orders:
        order_dict = {'product name': order.product_name, 'cost': str(order.cost), 'quantity': order.qty}
        order_dicts.append(order_dict)

    return json.dumps(order_dicts, indent=1)
