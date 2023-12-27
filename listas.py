
print("LISTAS")
mi_lista=list()
mi_otra_lista = []



print("los datos en una lista entrar desde la posicion 0 consecutivamente")
print("Longitud de la lista")
print(len(mi_lista))
mi_lista=[25,24,62,55,30,30,17]
print(mi_lista)
print(len(mi_lista))

mi_otra_lista=[55, 1.84,"Ignacio","Lorduy"]
print(mi_otra_lista)
print("imprimir un elemento concreto de una lista, se puede hacer desde el primero o desde el ultimo con el simbolo -")
print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-3])
print("Utilizar count en una lista para contar el numero de veces que aparece algo, en este caso 2 veces ")
print(mi_lista.count(30))
print("Concatenar o sumar listar listas")
mi_tercera_lista=mi_lista+mi_otra_lista
print(mi_tercera_lista)
print("ñadir al final de la lista")
mi_tercera_lista.append("miempresa")
print(mi_tercera_lista)
print("inserter en una posicion de la lista")
mi_tercera_lista.insert(2,"Azul")
mi_tercera_lista.insert(4,"Azul")
print(mi_tercera_lista)
print("eliminar el primer coincidente de la lista")
mi_tercera_lista.remove("Azul")
print(mi_tercera_lista)
print("quitar el ultimo elemento de la lista y nos devuelve el valor eliminado")
print("vamos a eliminar el valor de la lista que es:")
var=(mi_tercera_lista.pop()) #guardamos el valor a la vez que eliminamos
print(var)
print(mi_tercera_lista)
print("vamos a eliminar el valor 2 de la lista que es:")
var=(mi_tercera_lista.pop(2)) #guardamos el valor a la vez que eliminamos
print(var)
print(mi_tercera_lista)
print("vamos a eliminar el valor 3 de la lista pero sin guardar:")
del mi_tercera_lista[3]
print(mi_tercera_lista)

print("vamos a cambiar el valor de un elemento de la lista:")
mi_tercera_lista[5]="XXXX"
print(mi_tercera_lista)
print("copiar una lista:")
mi_cuarta_lista=mi_tercera_lista.copy()
print("elimino el contenido de una lista")
mi_tercera_lista.clear
print(mi_cuarta_lista)
print("damos la vuelta a una lista")
mi_cuarta_lista.reverse()
print(mi_cuarta_lista)
print("hacemos ordenacion")
mi_lista.sort()
print(mi_lista)
print("saber el indice de un elemento dentro de una lista,buscamos el valor 30")
print(mi_lista.index(30))
print(mi_lista.index(30))