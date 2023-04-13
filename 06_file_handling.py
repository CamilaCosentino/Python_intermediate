##### File Handling #####
import os
# .txt file
# función para abri un fichero
txt_file = open(
    file="02_intermediate/my_file.txt", #se debe poner la ruta completa
    mode= "w+" # osea el w+ para escribir y leer, lo sobre escribe
    )

print(txt_file.read())
txt_file.write("Mi nombre es Camila\nMi apelido es Cosetino\nMi edad es 23 años\nMi lenguaje favorito es Python")
print(txt_file.read(10)) # lee los primeros 10 carecteres
print(txt_file.readline()) # lee una linea de fichero
print(txt_file.readlines()) # devuelve un loop dentro de una array

txt_file.write("\nAunque también me gusta JS") # escribir una linea
for line in txt_file.readlines(): # iterar con un for in el fichero x lineas
 print(line) 
txt_file.close()
with open(file="02_intermediate/my_file.txt",mode="a") as my_other_file:
    my_other_file.write("\n Y SQL")
#os.remove("02_intermediate/my_file.txt") # para eliminar el fichero

# .json file



import json #utilidad para trabajar con json

json_file = open(
    file="02_intermediate/my_file.json", #se debe poner la ruta completa
    mode= "w+" # osea el w+ para escribir y leer, lo sobre escribe
    )

json_test = {
    "name":"Camila", 
    "surname":"Cosentino",
    "age":"23",
    "languages":[
        "Python",
        "Nodejs",
        "Reactjs"
        ],
    "page":"www.ccporfolio.com"
    }
json.dump(json_test,json_file, indent=2) # se debe poner el diccionario y la ruta. La indent es cuantos espacios a la derecha queres ponerles
json_file.close() # si no lo cerramos no lo podemos leer
with open(file="02_intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines(): # iterar con un for in el fichero x lineas
        print(line) 
        
json_dict = json.load(open("02_intermediate/my_file.json")) # como pasar de un json a un dict.
print(json_dict) 
print(type(json_dict)) # dice que es una clase de tipo dict
print(json_dict["name"]) #podemos acceder a los valores de las claves del archivo


# .csv file
import csv
csv_file = open("02_intermediate/my_file.csv","w+")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["Camila","Cosentino","23","Python","www.ccporfolio.com"])
csv_writer.writerow(["Alexis","Gomez","23","Javascript",""])

csv_file.close()
with open("02_intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines(): # iterar con un for in el fichero x lineas
        print(line) 
# .xlsx file
# import xlrd debe instalar el modulo

#.xml file
import xml