
print("Son funciones que hacen llamadas a otras funciones ,algunas estan predefnidas por el sistema")

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, seccond_value, f_sum):
    return f_sum(first_value + seccond_value)

print("Al llamar a la funcion sum_two_values_and_add_values le estoy pasando como parametro otra segunda funcion, y luego la invoco dentro de la primera funcion ")
print("esta es la manera de que una funcion pueda invocar a otra funcion, porque si no se la pasamos no la reconoce dentro de su ambito")
print(sum_two_values_and_add_value(5,2,sum_one))
print(sum_two_values_and_add_value(5,2,sum_five))

print("CLOUSERS")
def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()    
print(add_closure(5))

print("FUNCIONES DE ORDEM SUPERIOR PROPIAS DEL SISTEMA")
print("Map")
print("a Map le pasamos una lista y una funcion y coge cada elemento de la lista y lo pasa por la funcion, devolviendo una lista con los nuevos valores")
numbers = [2,5,10,21,30]
def multiplicar_dos(numero):
    return numero * 2

print(list(map(multiplicar_dos, numbers)))

print("filter")
print("le podemos pasar una lista y una funcion que le devuelve verdadero o falso, y las que son Falso las quita de la lista que va a devolver")
def filtrar_valores_mayores_diez(numero):
     if numero > 10:
         return True
     return False    
print(list(filter(filtrar_valores_mayores_diez,numbers)))

print("reduce")
print("le podemos pasar una lista y una funcion, y el resultado de la funcion la va acumulando y al final devuelve un unico valor que es el sumatorio ")
from functools import reduce
numbers = [2,5,10,21,30]
def sumar_dos_valores(primer_valor,segundo_valor):
    print(primer_valor)
    print(segundo_valor)
    return primer_valor + segundo_valor

print(reduce(sumar_dos_valores,numbers))
