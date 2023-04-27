from pathlib import Path
from time import ctime

archivo = Path('gestion_de_archivos/archivo.txt')

# archivo.exists()
# archivo.rename()
# archivo.unlink()
# print(archivo.stat())
print("acceso", ctime(archivo.stat().st_atime))
