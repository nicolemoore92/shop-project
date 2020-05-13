def save_orders_to_json(orders, filename = 'order_data.json'):
    order_dicts = []
    for order in orders:
        order_dict = {'product name': order.product_name, 'cost': str(order.cost), 'quantity': order.qty}
        order_dicts.append(order_dict)
    with open(filename, 'w') as od:
        json.dump(order_dicts, od, indent=1)
