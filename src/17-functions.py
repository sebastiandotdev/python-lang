## Funtions ##

"""
  todo: sintaxis de una funcion
 """
def my_function ():
    """
      ? bloque de una funcion
    """
    my_greet = input("ingresa tu numero: ")
    if my_greet.isdigit():
      print(f'tu numero: {my_greet}')
    else:
        print("numero invalido")  

        

"""
  ! invocacion de una funcion
  Returns:
  _type_: _description_
 """
my_function()


"""
  todo: parametros de una funcion
"""
def sum (a,b):
    """

    Args:
      a (int): numero 1
      b (int): numero 2

   Returns:
      _int_: _devolver la suma_
    """
    return a + b

print(sum(1,2))
print(sum(3221,2221))
print(sum(3221,1.2))


def greet(name, lastname):
    return f'{name} {lastname}'

print(greet('sebastian', 'castro'))

def isValid (cardNumber):
    if cardNumber != "int":
        print("ingresa un numero")
    else:
        my_number = input("dime el numero")
        return my_number

isValid(20)    


def is_number (): 
    num = input("ingresa un numero: ")
    if num.isdigit():
        value = num
        print(f"el numero ingresado es : {value}")
    else:
        print("La entrada no es un numero valido")        

is_number()


### parametro rest

def my_text (*text):
    return text

print(my_text("sebastian", "hola", "python"))