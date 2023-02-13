### List ###


my_list = list()
print(type(my_list))

my_other_list = []
print(type(my_other_list))
print(len(my_other_list))

my_list = [20 , 28, 30, 19, 10 , 17]
print(my_list)
print(len(my_list))

my_other_list = [18 , 1.69, 'sebastian', 'castro', ['list', 'other']]
print(my_other_list)
print(len(my_other_list))

age, tall,name,lastname, data = my_other_list
print(f'hi esta es mi edad: {age} , mi altura: {tall} , mi nombre: {name} , {data}')

print(my_other_list[-1])
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[-1][0])

print(my_list + my_other_list)
# print(my_list - my_other_list) 
# print(my_list * my_other_list) ERROR
# print(my_list / my_other_list)

# metodos

my_list_sebastian = ['sebastian', 'castro']
my_list_sebastian.append(18) # append // agrega un elemento a la lista
print(my_list_sebastian)

my_list_sebastian.insert(0, 'este es el insert') # insert // inserta un elemento de acuerdo a una posicion que le asignes
print(my_list_sebastian)

my_list_sebastian[1] = 'johan sebastian'
print(my_list_sebastian)

my_list_sebastian.remove('este es el insert') ## remove dile el elemento y el lo eliminara
print(my_list_sebastian)

"""Este es un comentario en python para documentar"""
my_list_sebastian.pop()
print(my_list_sebastian)

"""reverse invierte los valores"""
my_list_sebastian.reverse()
print(my_list_sebastian)

"""
  _summary_
  documentacion en python importante
"""
my_list_sebastian.sort()
print(my_list_sebastian)
"""
  provamos diferentes metodos de una lista
 """
del my_list_sebastian[1]
print(my_list_sebastian)

my_new_list = my_list_sebastian.copy()
print(my_new_list)


my_list_sebastian.clear()
print(my_list_sebastian)

