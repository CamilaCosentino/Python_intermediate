### List Comprehension ###
# se utiliza para crear listas rápído o crear lista que ya tengamos
my_original_list = [0,1,2,3,4, 5,6,7]
my_list = [i for i in range(8)] # palabra reservada i (for in), range() te genera un rango de 0 a numero que pongas, en este caso 8
print(my_list)

my_range = range(10)
print(list(my_range))

my_list =  [i + 1 for i in range(8)] # esto lo que va a ser es sumarle un elemento a la lista
print(my_list)

my_list =  [i * 2 for i in range(8)] # al elemento va a multiplicarlo x2 
print(my_list)


my_list =  [i * i for i in range(8)] # poniedo i * i se va a multiplicar por si mismo
print(my_list)

def sum_five(number):
   return number + 5



my_list =  [sum_five(i) for i in range(8)] # a cada elemento se le suma 5, se modifica el valor antes de guardarlo
print(my_list)