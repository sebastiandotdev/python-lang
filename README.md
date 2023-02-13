# python

- python es un lenguaje de programacion open source que es capaz de hacer muchas cosas en la capas de la progrmacion su enfoque es ciencia de data y machine learning pero tambien puede ejecutarse en el navgeador

- python es dinamico su valor puede ir cambiando mediante el proceso y flujo de su programacion

# Funciones Built-in

- estas son las operaciones mas importante que ya tienen precargada el sistema nosotros podemos llamarla directamente passarle un parametros no depende de un un tipo de dato

- El intérprete de Python tiene una serie de funciones y tipos incluidos en él que están siempre disponibles. Están listados aquí en orden alfabético

```
A

abs() --retorna el numero absoluto
aiter()
all()
any()
anext()
ascii()

B

bin()
bool()
breakpoint()
bytearray()
bytes()

C

callable()
chr()
classmethod()
compile()
complex()

D

delattr()
dict()
dir()
divmod()

E

enumerate()
eval()
exec()

F

filter()
float()
format()
frozenset()

G

getattr()
globals()

H

hasattr()
hash()
help()
hex()

I

id()
input() --recibe un dato y lo devuelve
int() -- transforma un numero de string a una entero
isinstance()
issubclass()
iter()

L

len() -- cuenta los caracteres de una cadena de texto
list()
locals()

M

map()
max()
memoryview()
min()

N

next()

O

object()
oct()
open()
ord()

P

pow()
print() -- nos muestra el dato por la shell
property()

R

range()
repr()
reversed()
round()

S

set()
setattr()
slice()
sorted()
staticmethod()
str() -- transforma un numero a un string
sum()
super()

T

tuple()
type()

V

vars()

Z

zip()

_
__import__()
```

## tipos de datos

- python tiene los siguientes tipos de datos:

* string
* number
* boolean
* list
* tuple
* dictonaries
* none

## varaibles

- en python no requiere de una palabra reservada para nombrar una variable , es importante seguir las conveciones en las vairbles python nos dice que usemos la declaracion de una variable en minuscula y en snake_case

```
    name
    lastname

    my_name
    my_lastname
```

### variables mal escritas

```
    my-name
    first@name
    num-1
    1-num
```

## metodos string

1. str.upper(): convierte todos los caracteres de una cadena a mayúsculas.

2. str.lower(): convierte todos los caracteres de una cadena a minúsculas.

3. str.capitalize(): convierte el primer carácter de una cadena a mayúsculas y el resto a minúsculas.

4. str.strip(): elimina los espacios en blanco de ambos extremos de una cadena.

5. str.replace(old, new): reemplaza todas las apariciones de old en una cadena con new.

6. str.split(sep): divide una cadena en una lista de subcadenas, utilizando sep como separador.

7. str.format(): permite insertar valores dentro de una cadena, utilizando {} como marcadores de posición.

8. str.join(iterable): une todas las cadenas en un iterable (como una lista o una tupla), separándolas con la cadena sobre la que se llama al método.

Estos son solo algunos de los métodos más comunes de cadenas de caracteres en Python. Hay muchos otros que se pueden usar para realizar diversas tareas con cadenas de caracteres. Es importante que los conozcas y los entiendas bien para poder aprovechar al máximo las funcionalidades de Python.

## operadores y numeros

```
=	x = 5	x = 5
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3
%=	x %= 3	x = x % 3
//=	x //= 3	x = x // 3
**=	x **= 3	x = x ** 3
&=	x &= 3	x = x & 3
|=	x |= 3	x = x | 3
^=	x ^= 3	x = x ^ 3
>>=	x >>= 3	x = x >> 3
<<=	x <<= 3	x = x << 3
```

## List

- En programación, un "array" y una "lista" son términos que a menudo se utilizan para describir colecciones de datos similares, pero en realidad existen algunas diferencias importantes entre ellos.

Un "array" es una estructura de datos en la que se almacenan elementos de un mismo tipo y tienen un tamaño fijo. Una vez que se ha definido el tamaño de un array, no se pueden agregar o quitar elementos, a menos que se cree un nuevo array con un tamaño diferente. Las operaciones en un array son generalmente más rápidas que en una lista debido a su estructura de datos contigua en la memoria.

Por otro lado, una "lista" es una estructura de datos dinámica en la que los elementos se almacenan de forma no contigua y se pueden agregar y quitar elementos en cualquier momento. Las listas también permiten almacenar elementos de diferentes tipos y pueden tener un tamaño ilimitado. Las operaciones en una lista son un poco más lentas que en un array debido a la complejidad de su estructura de datos, pero son más flexibles y versátiles.

```
Hay muchos métodos que se pueden utilizar en una lista de Python, pero aquí hay algunos de los más importantes:

append(element): Agrega un elemento al final de la lista.

extend(iterable): Agrega todos los elementos de un objeto iterable (como una lista) al final de la lista.

insert(index, element): Inserta un elemento en una posición específica en la lista.

remove(element): Elimina el primer elemento de la lista que sea igual al elemento especificado.

pop(index): Elimina el elemento en una posición específica en la lista y lo devuelve.

index(element): Devuelve el índice del primer elemento en la lista que sea igual al elemento especificado.

count(element): Devuelve el número de veces que aparece un elemento específico en la lista.

sort(): Ordena los elementos de la lista en orden ascendente.

reverse(): Invierte el orden de los elementos en la lista.

clear(): Elimina todos los elementos de la lista.

Estos son solo algunos de los métodos más comunes que se pueden utilizar en una lista de Python. Hay muchos otros métodos y funciones que se pueden aplicar a las listas en Python, dependiendo de tus necesidades específicas.

```

## tuple

- Las tuplas en Python son un tipo de datos inmutable, por lo que no se pueden modificar sus valores una vez que se han creado. Sin embargo, existen algunos métodos que puedes utilizar para trabajar con tuplas. Aquí están algunos de los métodos más importantes:

```
count(value): Devuelve el número de veces que un valor determinado aparece en una tupla.

index(value): Devuelve el índice del primer elemento que coincide con el valor especificado.

len(): Devuelve el número de elementos en una tupla.

tuple(): Convierte una secuencia en una tupla.

min(): Devuelve el elemento mínimo en una tupla.

max(): Devuelve el elemento máximo en una tupla.

sorted(): Devuelve una nueva tupla con los elementos ordenados.
```
