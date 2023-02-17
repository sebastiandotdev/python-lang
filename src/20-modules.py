""" # modulo completo"""

import myModule
import math
import random
import os

result = myModule.sum(2, 4)
resultOne = myModule.res(1, 4)
sebas = myModule.Sebastian
try: 
    print(result)
    s = sebas("sebas")
    print(s.name)
    print(math.pi)
    num = random.random() * 100
    print(num)
    files = os.mkdir("hola")
    print(files)
except TypeError as e:
    print(e)    
