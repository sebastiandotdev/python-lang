## variables y constante con python

""" 
TODO: VARIABLES EN PYTHON
! python no usa ninguna palabra reservada para definir una variables , al momento de tu asignarle un valor a cualquier cosa que escribas en tu editor de codigo , excepto las palabras reservada ya es una variable
"""

""" 
? variable name con mi nombre = :)
"""
name = 'sebastian'
print(name)

""" 
? variable number
"""
number = 100
print(number)

""" 
? variable booleana
"""
boolean = True
print(boolean)

""" 
? variable de lista
"""
check = [100,200,300]
print(check)

oss = ('s', 'e', 'b', 'a', 's', 't', 'i', 'a', 'n')
print(oss)


sebastian = {
    "name": "sebastian",
    "lastname": "castro",
    "surnmae": "SS9139"
}
print(sebastian)


## variables de una linea
book, link = 'join cheeck', 'http://3000'
print(book)
print(link)


# conveciones

""" 
! Luego de aver defino unas cuantas variables , tenemos las conveciones en python es buena practica usar snake_case
"""
book_name = '''703'''
print(book_name)

bookName = '''703'''
print(bookName)

BookName = '''703'''
print(BookName)

PI = 3.1416
print(PI)

# snake case

""" 
! miren mas bonito , va mas con el lenguaje
"""
my_string_variables = 'sebastian'

my_int_variables = 20

my_bool_variables = True

print(str(f'my name is {my_string_variables}'))
print(str(my_int_variables))


## forzar tipado ? 
""" 
! es de tipado dinamico :0, eso me sorprendio !!
"""
address: str = 'mi dirrecion'
address = 10
address = True
address = 1.2
print(type(address))