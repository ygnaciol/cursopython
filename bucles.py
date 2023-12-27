var=0
print("A los bucles while puedes meterles un else al final, ahunque es poco habitual")
while var < 10:
    print(var)
    var=var+1
else: #es opcional
    print("entro por el else del while")
    print("el valor de var es",var)
print ("termino")


var=0
print("Interrumpir un bucle")
while var < 10:
    print(var)
    var=var+1
    if var == 5 :
        print ("Se detuvo con break en el numero: ",var)
        break
       
print("bucle for recorriendo una LISTA")
print("tambien se puede meter un else en un bucle for, y tambien meter un break")
mi_lista=[25,24,62,55,30,30,17]
for elementos in mi_lista:
    print(elementos)

print("bucle for recorriendo una TUPLA")
mi_tupla=(55,1.84,"Ignacio","Lorduy")
for elementos in mi_tupla:
    print(elementos)

print("bucle for recorriendo un SET")
my_set={"a","b","c","pepe"}
for elementos in my_set:
    print(elementos)
print("bucle for recorriendo un DICCIONARIO y mostrando sus cabeceras")
my_dic={"Nombre":"Ignacio","Apellido":"Lorduy","Edad":55,1:"Python"}
for elementos in my_dic:
    print(elementos)

print("bucle for recorriendo un DICCIONARIO y mostrando sus cabeceras y sus valores")
my_dic={"Nombre":"Ignacio","Apellido":"Lorduy","Edad":55,1:"Python"}
for elementos in my_dic.items():
    print(elementos)
   

print("bucle for recorriendo un DICCIONARIO y mostrando sus valores")
my_dic={"Nombre":"Ignacio","Apellido":"Lorduy","Edad":55,1:"Python"}
for elementos in my_dic.values():
    print(elementos)
   
print("bucle for recorriendo un DICCIONARIO y utilizando CONTINUE, No se utiliza")
my_dic={"Nombre":"Ignacio","Apellido":"Lorduy","Edad":55,1:"Python"}
for elementos in my_dic.values():
    print(elementos)
    if elementos == "Edad":
        print ("Ha entrado por continue, por lo que el bucle a continuado")
        print("CONTINUE en ese momento y envia el cursor")
        print("al principio del bucle desde el siguiente elemento que toca")
        continue
   