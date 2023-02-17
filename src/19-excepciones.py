### excepciones ###


numOne,numTwo = 1, 5
numOne = "2"

try:
    print(numOne + numTwo)
    print("no se ha producido error")
except:
    print("se ha producido un error")    

try:
    print(numOne + numTwo)
except TypeError:
    print(" hubo un error")       

try:
    print(numOne + numTwo)
except TypeError as error:
    print(error)       

try:
    print(numOne + numTwo)
except ValueError as error:
    print(error)

"""
 # manejo de errores con alias
"""
try:
    print(numOne + numTwo)
except ValueError as e:
    print(e)