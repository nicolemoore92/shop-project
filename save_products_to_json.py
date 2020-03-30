import json

def save_products_to_json(products, filename = 'product_data.json'):
      product_dicts = []
      for product in products:
          product_dict = {'name': product.name, 'cost': str(product.cost), 'description': product.description}
          product_dicts.append(product_dict)
      with open(filename, 'w') as pd:
          json.dump(product_dicts,pd, indent=1)
