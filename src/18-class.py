# class #

"""
  todo: sintaxis de una class
"""
class MyClass:
    """
    ? la palabra pass evita que se ejecute la clase
    """
    pass

print(MyClass)

class Greet: 
    """
      todo: la palabra init es el contructor de la class
    """
    def __init__(self, greet, name):
        self.greet = greet
        self.name = name

sebastian = Greet("hola" , "sebassstian")
print(f"{sebastian.greet} {sebastian.name}")    



class Perro: 
    def __init__(self, name, lastname):
        self.full__name = f"{name} {lastname}"


dog = Perro("snow", "sgooy")
print(dog.full__name)


## metodos


class Person: 
    def __init__(self, name, lastname):
        self.full__name = f'{name} {lastname}'

    def walk(self):        
        return f"{self.full__name} esta caminando"

joan = Person("johan", "castro")
print(joan.walk())



class Car:
    def __init__(self, mark, color, fast):
        self.mark = mark
        self.color = color
        self.fast = fast

    def full__car (self, model):
        self.model = model
        return f"{self.mark} {self.color} {self.model}"
    
    def get__model (self):
        return f"{self.model}"
    
    def get__color (self):
        return f"{self.color}"
        
mercede = Car("mercede", "blue", "160km")
print(mercede.full__car("2021"))
print(mercede.get__color())
print(mercede.get__model())


class Movies: 
    def __init__(self, name, gene, year , IMDB):
        self.name = name
        self.gene = gene
        self.year = year
        self.IMDB = IMDB


my_movies = [
    {
        "id": 1,
        "name": "the batman",
        "gene": "aventures",
        "year": "2022",
        "IMDB": "20001T"
    }
]

for movie in my_movies: 
    batman = Movies(movie["name"], movie["gene"], movie["year"],movie["IMDB"])
    print(f"name: {batman.name} gene: {batman.gene} year: {batman.year}")

