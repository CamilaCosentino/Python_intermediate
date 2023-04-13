##### Regular Expressions #####
# Las regex (en inglés, regular expressions) son las unidades de descripción de los lenguajes regulares, que se incluyen en los denominados lenguajes formales. Son un instrumento clave de la informática teórica, la cual, entre otras cosas, establece las bases para el desarrollo y la ejecución de programas informáticos, así como para la construcción del compilador necesario para ello. Es por esto que las expresiones regulares, también denominadas regex y basadas en reglas sintácticas claramente definidas, se utilizan principalmente en el ámbito del desarrollo de software.
# nos sirve para expeccionar si una cadena de texto tiene o no ciertos elementos, además devuleve las recundencias de los que estamos pasando.
# Estudiar el concepto de expresiones reguralares - IMPORTANTE
# Permiten filtrar textos para encontrar coincidencias, comprobar la validez de fechas, documentos de identidad o contraseñas, se pueden utilizar para reemplazar texto con unas características concretas por otro, y muchos más usos.
import re # todas las funcionalidades de las expresiones regulares
## Match
my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"
match =  re.match("Esta no es la lección", my_other_string)
#if not(match == None): # otra forma de validar no es un None
#if match != None: # otra forma de validar no es None
if match is not None: # otra forma de validar que no es None
    print(match)
    print(match.span()) #devuelve entre que caracteres se encuentra el matcheo, intenta aplicar un patrón al comienzo del string y devuelve si lo encuentra o no(si es false devuelve None)
    start, end = match.span() # es una tupla formada por el n° de caracter que empieza y con el que termina
    print(my_other_string[start:end]) # se nos muestra el string que encierra todo desde la primera y la última posición del match

#print(re.match("Expresiones Regulares", my_string)) # devuelve None porque empieza a buscar desde el principio}
# revisar los parametros de adentro.

## Search
# objeto match que devulve lo mismo que match, pero se puede encontrar una cadena de texto de cualquier parte del string no solo del comienzo como el match
search = re.search("lección", my_string, re.I)
print(search)

## Findall
# genera un listado con la cantidad de veces que encuentra el valor. No importa si está uppercase o en lowcase pero si cambia si le falta la tilde
findall = re.findall("lección", my_string, re.I)
print(findall)

## Split 
# genera un lista y separa según el primer argumento (el cual es el separador.)
split = re.split(":",my_string) 
print(split)

## Sub
# se usa para subtituir un valor
# primer arg = valor a modificar , segundo arg = valor que lo va a remplazar y el tercero la cadena de texto en este caso.
sub = re.sub("Expresiones","expresiones", my_string)
print(sub) # te devuelve los valores modificados
print(re.sub("lección","LECCIÓN", my_string)) # solo toma en cuenta el valor inicial (osea la primera.)
print(re.sub("Expresiones Regulares","RegEx", my_string))
print(re.sub("lección|Lección","LECCIÓN", my_string)) # si nosotros usamos | para los 2 valores, se modifican ambos.
print(re.sub("[lL]ección","LECCIÓN", my_string)) # también se puede encerrar las lL entre [] y así que lo tome indefinidamente si está la L en uppercase o en lowcase 

## Patterns
pattern = r'[lL]ección' # incluir la r y entre comillas el patron que queremos encontrar
print(re.findall(pattern,my_string))

pattern =  r'[lL]ección|Expresiones' # se puede incluir más de un patron utilizando |
print(re.findall(pattern,my_string))

pattern =  r'[a-z]' # busca todas la palabras a-z, no incluyen las vocales con tildes
print(re.findall(pattern,my_string))

pattern =  r'[0-9]' # busca todas la palabras 0-9 y en este caso devuelve un 7
print(re.findall(pattern,my_string)) # 7
print(re.match(pattern,my_string)) # None
print(re.search(pattern,my_string)) 

pattern =  r'[0-5]' # busca todas la palabras 0-5 y en este caso devuelve un []
print(re.findall(pattern,my_string))
print(re.match(pattern,my_string)) # None


pattern =  r'\d' # devuelve un 7 porque esta regex busca si existe dígitos
print(re.findall(pattern,my_string))

pattern =  r'\D' # devuelve todas las letras menos los numeros
print(re.findall(pattern,my_string))


pattern =  r'[l].' # devuelve todas las silabas que contengan l dentro de la cadela de texto
print(re.findall(pattern,my_string))

pattern =  r'[l].*' # en este caso, como puse l comieza a mostrar desde la 1era l para adelante, es decir toda la cadela de text
print(re.findall(pattern,my_string))


# email validator regular expresion
email =  'gz.alexis2@gmail.com'
pattern = r'^[a-zA-z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+$'
"""
^ = empieza por..
[a-zA-z0-9_.+-] = que contenga letras de a-z tanto uppercase y/o lowcase, numeros del 0-9, caracteres como _ . + -
+@ =  que contenga una @.
[a-zA-Z0-9-] =  parecido comom arriba pero solo caracteres alfanúmericos (a-z y 0-9)
\  =  se utiliza para escapar caracteres
. =   cualquier carácter excepto el carácter de nueva línea (\n) 
$ = termina con.. , va a tener en cuenta todo lo que esta por detras mientras pongamos el . (en este caso)
"""

print(re.match(pattern,email)) 
print(re.search(pattern,email)) 
print(re.findall(pattern,email)) 


