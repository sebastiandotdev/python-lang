from myModule import sum,res,Sebastian
from math import pi as PI

try:
 result =  res (1, 2)
 print(result)
except TypeError as e:
  print(e)  
    

try:
 result = Sebastian("johan")
 print(result.name)
 print(PI)
except TypeError as e:
  print(e)  