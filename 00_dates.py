##### DATES ######
# modulo nativo de python podemos extraer solamente las funciones que queramos de está forma
from datetime import datetime, time, date, timedelta
# siempre hay que inicializar }
now= datetime.now()

timestamp = now.timestamp()
print(timestamp) # representación única para el tiempo, más fácil para base de datos.
# función para crear una fecha personaizada y acceder a los valores que componen esa fecha
def print_date(date) : 
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

# se puede acceder a los datos de la fecha actual


# fecha en base a datos
year_2023 = datetime(2023,7,12) # los argumentos de año, mes y día (si no incluis horario se pone 00:00:00) 
print_date(year_2023)

# time no se puede inicializar con la hora actual como puede ser datetime y date
current_time = time(20,46,34) # si lo dejas vacio te va a devolver 0 en cada valor
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
# time hay datos que faltan ya que solo se puede usar para horarios.
# hay q empezar a hace operaciones para acceder los datos porque está vacio a comparación de datetime.
# es un objeto que es capáz de guardar tiempo
# ver siempre la documentación
# el datetime y el time son diferentes funciones o metodos

today =  date.today() # el today toma la fecha de hoy en formato YYYY-MM-DD
print(today)
# date sirve para devolver fechas no tiempo por eso lo excluye
# es un objeto que necesita argumento año, mes y día como obligatorios, NO PUEDE MANDAR date() sin nada porque salta ese error
current_date = date(2023,7, 12)# se tiene que pasar el mes con un solo dígito aunque el formato sea con 2
print(current_date) 
print(current_date.year)
print(current_date.month)
print(current_date.day)


# se puede pasar una fecha personalizada y acceder a sus valores

## Modificar fecha
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

## restando datetime- diferencia
diff = year_2023 - now
print(diff)

# restando date - diferencia
diff = year_2023.date() - current_date  # se le pone .date() porque year_2023 es un date time
print(diff)

# restando time - diferencia
# diff = year_2023.time() - current_time  salta error cuando se usa con time 
# print(diff)

# TIME DELTA
# se usa para sacar diferencias entre frangas de fechass
start_timedelta = timedelta(200,100,100,weeks=5)
end_timedelta = timedelta(200,100,100,weeks=15)
print(end_timedelta - start_timedelta) 
print(end_timedelta + start_timedelta) 