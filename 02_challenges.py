### Challenges ####
""" EL FAMOSO "FIZZ BUZZ”
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def fizz_buzz_fun():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0: # se evalua primero este porque es el que tiene más retricciones
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz_fun()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(str1,str2):
    if str1.lower() == str2.lower():
        return False
    return sorted(str1.lower()) == sorted(str2.lower()) # sorted() crea un array de carateres, los ordena y compara

print(is_anagram("Cami","Mica"))


"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    prev = 0
    next = 1
    
    for i in range(50):
       
        print(prev)
        fib = prev + next
        prev = next
        next = fib
        


fibonacci()


"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""

def is_prime():
    for num in range(1,101):
        
        if num >= 2:
            is_divisible = False
            for i in range(2,num):
                 if num % i == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(num)
    
is_prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(str):
    reversed_string = ""
    text_len = len(str)
    for i in range(0, text_len):
      reversed_string += str[text_len - i - 1]
    return reversed_string
print(reverse("Hola Mundo"))