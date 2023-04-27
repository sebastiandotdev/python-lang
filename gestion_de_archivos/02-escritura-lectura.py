from pathlib import Path

archivo = Path('gestion_de_archivos/archivo.txt')

texto = archivo.read_text("utf-8").split("\n")

texto.insert(0, 'sebastian')

archivo.write_text("\n".join(texto), 'utf-8')
