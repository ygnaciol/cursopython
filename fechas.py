
#asi importamos todo el modulo completo
#import datetime
#datetime.datetime.date
#print(vahora)

#asi importamos la partes del modulo que nos interesa concretamente
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta  #para operar con time
def imprimir_fecha(vfecha):
    print(vfecha.year)
    print(vfecha.month)
    print(vfecha.day)
    print(vfecha.hour)
    print(vfecha.minute)
    print(vfecha.second)
    print(vfecha.timestamp())
   

print("capturarmos la fecha en este momento")
vfecha=datetime.now()
print("imprimimos ayo,mes,day,hora,min.seg utilizando la funcion vfecha")
imprimir_fecha(vfecha)

print("representacion unica de un momento concreto en el tiempo")
tiempoenestemomento=vfecha.timestamp()
print(tiempoenestemomento)

print("crear una fecha")
año_2023=datetime(2023,1,1,14,30,57)
print("imprimimos ayo,mes,day,hora,min.seg utilizando la funcion vfecha")
print(año_2023)
imprimir_fecha(año_2023)

############################
print("utilizando el time")
tiempo_actual=time(21,6,58)
print(tiempo_actual.hour)
print(tiempo_actual.minute)
print(tiempo_actual.second)

fecha_actual=date(2023,1,1)
print(fecha_actual.year)
print(fecha_actual.month)
print(fecha_actual.day)

print(("Utilizando timedelta"))
star_timedelta=timedelta(200,100,100,weeks=10)
end_timedelta=timedelta(300,100,100,weeks=13)
print("restando y sumando fechas")
print(end_timedelta-star_timedelta)
print(end_timedelta+star_timedelta)


#funfion para calcular que dia sera dentro de x dias
def quediaseraeldia(dias):
    import datetime  #importamos el modulo completo
    fecha_actual = datetime.date.today()
    print(f"Sumar {dias} días a la fecha actual")
    fecha_nueva = fecha_actual + datetime.timedelta(days=dias)
    print("Imprimir la fecha resultante")
    print("Fecha actual:", fecha_actual)
    print(f"Fecha después de sumar {dias} días:", fecha_nueva)

var1=input("cuantos dias quieres sumar a la fecha actual:.....")
var1=int(var1)
quediaseraeldia(var1)