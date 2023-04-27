from io import open

texto = 'holas'

# archivo = open('gestion_de_archivos/hola-archivo.txt', 'w')

# archivo.write(texto)
# archivo.close()

# archivo = open('gestion_de_archivos/hola-archivo.txt', 'r')

# texto = archivo.read()
# archivo.close()
# print(texto)


with open('gestion_de_archivos/hola-archivo.txt') as archivo:
    texto = archivo.read()
    print(texto)
