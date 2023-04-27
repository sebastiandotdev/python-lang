import json
from pathlib import Path


products = [
    {'id': 1, 'name': 'mouse'},
    {'id': 2, 'name': 'wifi'},
    {'id': 3, 'name': 'keyboard'},
]

data = json.dumps(products)
print(data)

Path('gestion_de_archivos/products.json').write_text(data)
