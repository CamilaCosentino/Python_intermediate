##### Higher order functions #####
# son funciones que hacen cosas con funciones dentro. También hay funcionar dentro del sistema

def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


# f_sum es para pasar una función predefinida
def sum_two_values_and_add_value(first_value, second_value, f__sum):
    return f__sum(first_value + second_value)


# se puede pasar una funcion como argumento
print(sum_two_values_and_add_value(5, 5, sum_one))
print(sum_two_values_and_add_value(5, 5, sum_five))

##### Closures #####
# también hace ref a las funciones de orden superior pero con una peculiariadad
# nos vale para montanr paradigmas asigcronos, como listeners
# retorna una función 

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    
    return add

add_closure = sum_ten(2) # si se pone un parametro dentro de la función sum_ten lo toma de contexto
print(add_closure(6))
print((sum_ten(4)(5))) # se puede llamar igual que como una lambda. Inicialmente estamos haciendo, al sum_ten le pasamos un value y después seguimos concatenando 


##### Build-in Higher order functions #####
# funciones de ordenes superior dentro de sistema
numbers = [14,34,15,26]
def multiply_values(num):
    return num * 2
# Map
# va a necesitar como primer paramentros una funcion y después un interable(lista), y eso crea un interable 
print(list(map(multiply_values, numbers))) # aca creamos una lista y hacemos un map para que multique los valores
# las funciones de orden superior se pueden incluir funciones a traves de los argumentos
# map es un objeto

print(list(map(lambda num: num *3 , numbers))) # creamos una lambda y la operamos dentro del map para multiplicar x 3

# Filter
# va a necesitar como primer paramentros una funcion y después un interable(lista)
# tiene que ser una funcion que devuelva un boolean y crea una lista a partir de eso.
def filter_greater_than_twenty(num):
    if num > 20:
        return True
    return False
    
print(list(filter(filter_greater_than_twenty,numbers)))
print(list(filter(lambda num: num >=15,numbers))) # creamos una lambda y la operamos para que cree una lista con los values mayores y/o igual a 15

# Reduce
# va a necesitar como primer paramentros una funcion y después un interable(lista)
# operar entre los valores que va recorriendo un iterable 
# está en un modulo diferente hay que importarlo
# solo toma 2 parametros, y en este caso va sumando cada 2 valores por vez y después devulve el total.
from functools import reduce

def sum2values(fv,sv):
    return fv + sv
print(reduce(sum2values,numbers))