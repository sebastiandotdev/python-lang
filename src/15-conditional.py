""" @ conditionales en python """

my_condtion = False
my_age = 17


if my_condtion: 
  """ 
    ! Es importante el ordenamiento de codigo en python
  """
  print("la variable es true")


if my_age < 18:
  """ 
    ? usando los operadores logicos
  """
  print("eres menor de edad")

if my_age <= 18:
  """ 
  ? probando el menor e igual
  """
  print("eres menor de edad")


if my_age == 18:
  """ 
  ? probando el igual e igual
  """
  print("eres menor de edad")



if my_age >= 18:
  """
  ? mayor e igual
  @ validar la edad 
  """
  print("eres menor de edad")


if my_age == 17:
  """  
     ! probando el else
  """
  print("tienes 17 años")
else: 
  """
  ? si no se cumple
  """
  print("eres mayor a 17")


## acostumbrandome a la sintaxis

if my_age == 17 and my_age < 18:
  """ 
    TODO: doble condicion con el ampertans
  """
  print("es igual a 17")
else: 
  """
  ? si no se cumple , pero con el (and) debe cumplirse ambas funciones
  """
  print("no se ha cumplido la condicion")

if my_age <= 17 or my_age >= 18:
  """
  ! el or toma cualquiera de ambas condiciones
  """
  print("probando el or")
else: 
  print("ninguna se cumple")


## else if

"""
TODO: probando else if
"""
if my_age > 19:
  print("holaaa")
elif my_age < 19:
  print("este es el else")
else:
  print("finalizando con el else")


## ejercicios

is_valid = input("ingresa tu nombre: ")


if is_valid == "sebastian":
  print(f"bienbenido {is_valid}")
  my_plase = input("en que puedo ayudarte: ")
  if my_plase == "agua":
    print("si claro aqui tienes <3")
  else:
    my_prooduct = input("porfavor pide otro producto: ")
    if my_prooduct == "yogurt":
      print("listo fin de la IA")
    else:
      print(f"solo hay {my_plase} y {my_prooduct}")
else: 
  print("admin no identificado")


print("sigue la siguiente linea")