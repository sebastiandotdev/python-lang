
"""@ set en python"""
my_set = set()
print(type(my_set))

my_other_set = {'sebastian', 18}
print(type(my_other_set))

"""@ devuelve un boolean si existe el elemento"""
print('sebastian' in my_other_set) 
print(18 in my_other_set)


""" @ metodos de set """
my_other_set.add('castro')
print(my_other_set)

my_other_set.remove('castro')
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))


"""@ transformar un set a una list"""

my_set_ = {'johan', 'sebastian', 'castro', 'garcia'}
my_list_with_set = list(my_set_)

print(my_list_with_set)