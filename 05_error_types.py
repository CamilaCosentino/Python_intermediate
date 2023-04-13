##### Error Types #####

## SyntaxError
# print "Hola Comunidad" # Error:  Missing parentheses in call to 'print'. Did you mean print(...)? - Descomentar para Error
print("¡Hola Comunidad!") 


## NameError
language = "English" # Comentar para error
print(language) # NameError: name 'language' is not defined 


## IndexError
my_list  = ["Python","JavaScript","PHP","Java"]
print(my_list[0])
print(my_list[1])
print(my_list[-1])
# print(my_list[5]) # IndexError: list index out of range - Descomentar para Error


## ModuleNotFoundError
# import maths # ModuleNotFoundError: No module named 'maths' - Descomentar para Error
import math


## AttributeError
# print(math.PI) # AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'? -  Descomentar para Error
print(math.pi)


## KeyError
my_dicts = { "Nombre": "Camila","Apellido": "Cosentino", "Edad": 23, "Lenguages": {"Python", "Node.js", "JavaScript"},1: 1.63}
print(my_dicts["Edad"])
# print(my_dicts["Apelido"]) # KeyError: 'Apelido' - Descomentar para Error
print(my_dicts["Apellido"])


## TypeError
# print(my_list["0"]) # TypeError: list indices must be integers or slices, not str - Descomentar para Error
print(my_list[3])


# ImportError
# from math import pid # ImportError: cannot import name 'pid' from 'math' (unknown location) - Descomentar para Error
from math import pi
print(pi)


## ValueError
my_int = int("10")
# my_int = int("10 Años") # ValueError: invalid literal for int() with base 10: '10 Años' - Descomentar para Error
print(type(my_int + 1))


## ZeroDivisionError
print(4/2)
# print(4/0) # ZeroDivisionError: division by zero - Descomentar para Error

