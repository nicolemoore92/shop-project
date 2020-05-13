import json

def dump_products_to_json(products):
    product_dicts = []
    for product in products:
        product_dict = {'name': product.name, 'cost': str(product.cost), 'description': product.description}
        product_dicts.append(product_dict)
    return json.dumps(product_dicts, indent=1)
