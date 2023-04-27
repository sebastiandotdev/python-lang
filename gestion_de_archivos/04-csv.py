import csv


# with open('gestion_de_archivos/archiv.csv', 'w') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(['id', 'username', 'lastname'])
#     writer.writerow([1, 'sebastian', 'castro'])


with open('gestion_de_archivos/archiv.csv', 'r') as archivo:
    reader = csv.reader(archivo)
    archivo.seek(0)
    for line in reader:
        print(line)
