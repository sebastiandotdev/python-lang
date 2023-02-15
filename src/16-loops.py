""" # LOOPS """

my_condition = 0

"""
  !  while primer loops
"""
while my_condition < 10:
    """
        ? debe cumplirse esa condition
    """
    print("hola sebastian")
    my_condition += 2
    """
      todo: en python tenemos la oportunidad de usar un else en bucle si la condition no llega a cumplirse 

      ? esto lo hace interesante ya que tenemos la posibilidad de controlar el error
    """
else: # es opcional
    print("mi condition es mayor que 10 o igual")    


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("se detiene porque fue igual a 15")
        """
          ? de acuerdo a una condition acabamos con el bucle con la palabra reservada break
        """
        break
    print(my_condition)

print("-------------------------------------------------------")  

# FOR

data = [
  {
    "name": "sebastian",
    "lastname": "castro",
    "age": "18"
  },
  {
     "name": "ryan",
    "lastname": "dahl",
    "age": "28"
  },
  {
    "name": "joel",
    "lastname": "joe",
    "age": "22"
  }
]
my_tuple = ({"name": "sebastian"}, {"lastname": "castro"}, {"age": 18})
my_string = "sebastian"
my_dictonaries = {
    "name": "ryan",
    "lastname": "dahl",
    "age": "28"
}
"""
  todo: solo datos que son iterables
  ? tambieen podemos usar un else en el for loops
"""
for element in data:
    """
      ? se itera ddependiendo la cantidad de elemento que tengamos
    """
    print(element)

for element in my_tuple:
    print(element)

for element in my_string:
    print(element)

for element in my_dictonaries:
    if element == "name":
        print(element)
        """
        ! usando el break
        """
        break
else:
    print("el blucle for a finalizado de mi dictonaries")    

for element in my_dictonaries:
    if element == "name":
        print(element)
        """
        ! usando el continue
        """
        continue
else:
    print("el blucle for a finalizado de mi dictonaries") 




print("bucles finalizado")