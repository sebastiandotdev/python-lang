myStr = 'Jhon Doe'

name = 'sebastian'
lastname = 'castro'
vocabulary = 'A B C D F G H I J K L M N O P Q R S T U V W X Y Z'
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

## print(myStr.join())


print(f'Hi my name is {name} {lastname}')
print(name.upper().replace('SEBASTIAN', 'johan sebastian').count('a'))

print(f'este es el vocabulary:  {vocabulary.split()}')


# Desempaquetado de caracteres

my_languages = 'python'
p,y,t,h,o,n = my_languages

print(p, y, t ,h , o , n, '<3')

# Division

languaje_slice = my_languages[0:6]
print(languaje_slice)


slice_division = my_languages[3:4]
print(slice_division)

puntos_dobles_reverse = my_languages[::-1]
print(puntos_dobles_reverse)

elima_los_caracteres_agregado = my_languages[0:3]
print(elima_los_caracteres_agregado)

