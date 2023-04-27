import csv


with open('gestion_de_archivos/archiv.csv', 'w') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(['id', 'username', 'lastname'])
    writer.writerow([1, 'sebastian', 'castro'])
