
""" 
? tuplas en python
"""
my_tuple = tuple('holaa')
print(type(my_tuple))

my_person = ('sebastian', 18, 'castro')
print(my_person)
print(my_person[0])
print(my_person[1])
print(my_person[2])
print(my_person[-1])

""" suma de tupla """
full_tuple = my_tuple + my_person
print(full_tuple)

config_tuple = ('johan', 'sebastian', 'castro', 'garcia')

# config_tuple[0] = 'Joan'  error no puede cambiar valores

# metodos
print(config_tuple.count('johan'))
print(config_tuple.index('johan'))