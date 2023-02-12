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
