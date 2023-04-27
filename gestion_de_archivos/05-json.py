import json
from pathlib import Path


# products = [
#     {'id': 1, 'name': 'mouse'},
#     {'id': 2, 'name': 'wifi'},
#     {'id': 3, 'name': 'keyboard'},
# ]

# data = json.dumps(products)
# print(data)

# Path('gestion_de_archivos/products.json').write_text(data)

data = Path('gestion_de_archivos/products.json').read_text(encoding="utf-8")
products = json.loads(data)
print(products)
