##### Python Package Manager #####

# PIP
# Package instaler para python
# https://pypi.org/
# https://packaging.python.org/en/latest/tutorials/installing-packages/

# py -m pip --install pip
# py -m pip --upgrade pip 
# py -m pip --version


import numpy # py -m pip install numpy
""" es una biblioteca para el lenguaje de programación Python que da soporte para crear vectores y 
matrices grandes multidimensionales, junto con una gran colección de funciones matemáticas de alto nivel 
para operar con ellas.
"""
print(numpy.version.version)


numpy_array = numpy.array([10,43,65,87,44])
print(type(numpy_array))
print(numpy_array * 2)


# import pandas # py -m pip install pandas
"""
Pandas es una librería de Python especializada en la manipulación y el análisis de datos. 
Ofrece estructuras de datos y operaciones para manipular tablas numéricas y 
series temporales, es como el Excel de Python. Es un software libre distribuido bajo la licencia BSD
"""
# py -m pip list : se puede sacar un listado de los paquetes instalados
# py -m pip uninstall pandas(paquete) = para desinstalar algun paquete
# py -m pip show numpy =  muestra la información de ese paquete

#  py -m pip install requests
import requests
"""
Requests allows you to send HTTP/1.1 requests extremely easily. 
There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, 
just use the json method!
"""
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
#print(response.json())


## Arithmetics Package
# el __init__.py es lo que hace un paquete
from mypackage import arithmetics
print(arithmetics.sum(4,5))

from myotherpackage import other_arithmetics
print(other_arithmetics.multiply(5,7))
