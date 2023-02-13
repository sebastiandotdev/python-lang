""" @ DICTONARIES """

my_dict = dict()
print(type(my_dict))

my_other_dic = {}
print(type(my_other_dic))

my_other_dic = {
  "nombre": "sebastian",
  "edad": 18,
  "apellido": "castro",
  "address": {
    "manzana": "manzana",
    "calle": "cr27",
    "ciudad": {
      "colombia":"cesar"
    }
  },
  "lenguajes": ["typescript", "python"],
  10: ["azul", "gris"]
}
print(len(my_other_dic))
print(my_other_dic)

"""Acceder el valor de un dictonaries"""

print(my_other_dic["nombre"])
print(my_other_dic[10])
print(my_other_dic["address"]["manzana"])
print(my_other_dic["address"]["manzana"])
print(my_other_dic["address"]["ciudad"]["colombia"])


my_other_dic["add"] = "añadir datos a un dictonaries"
print(my_other_dic)


"""@ metodos"""

print("nombre" in my_other_dic)
print("no existe" in my_other_dic)

print(my_other_dic.items())
print(my_other_dic.keys())
print(my_other_dic.values())
print(my_other_dic.fromkeys("sebastian", 10))

my_other_dic["sebastian"] = "holaa"
print(my_other_dic)

del my_other_dic