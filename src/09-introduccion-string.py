myStr = 'Jhon Doe'

# print(dir(myStr)) ## la funcion dir nos dice que podemos hacer con el tipo de dato string


## metodo upper // convierte a mayuscula
print(myStr.upper())

## metodo lower // convierte a minuscula
print(myStr.lower())

## swapcase // convierte mayusculas y minuscula

print(myStr.swapcase())

## capitaliza // convierte la primera letra a mayuscula

print(myStr.capitalize())


## replace // remplaza un texto

print(myStr.replace('Jhon', 'Sebastian'))
print(myStr.replace('Jhon', 'Sebastian').upper())


## count // cuenta cuantas veces tenemos repetido una letra

print(myStr.count(' '))


## startsWith // nos dice si el caracter ingresado empieza por esa letra

print(myStr.startswith('Sebastian'))

## endsWith // nos dice si el caracter ingresado empieza por esa letra

print(myStr.endswith('Sebastian'))


## split // separa el texto en dos

print(myStr.split())


## find // busca un caracter

print(myStr.find('o'))


## len // cantidad de caracteres

print(len(myStr))


## index // me dice el indice de el caracter ingresado

print(myStr.index('o'))


## isnumeric // me dice si es un numero

print(myStr.isnumeric())
print(myStr.isalpha())


## posiciones

print(myStr[2])


## concatenacion

print('hi my name is Sebastian' + 'castro garcia')

## f // interpreta string

print(f'hi my name is {myStr}')


## forma // metodo de string que interpreta una variable en un string

print('my name is {0}'.format(myStr))


## strip // elimina los espacio en blanco en ambos extremos

print(myStr.strip())


## join // une toda la cadena

print(myStr.join())