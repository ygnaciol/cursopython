
print("LOS SET NO ADMITEN VALORES DUPLICADOS")
print("creamos un set")
my_set= set()
print("creamos un diccionario, porque set y diccionario se define igual")
my_otro_set = {}
print("convertimos ese diccionario a set en el momento que le metemos datos")
my_set={"a","b","c","pepe"}
my_otro_set={"Luis",2,4,5}
print(my_otro_set)
print("OJO: UN SET NO ES UNA ESTRUCTURA ORDENADA")
print("añadimos un elemento al set")
my_otro_set.add("pepe")
print(my_otro_set)
print("no puedes añadir el mismo elemento 2 veces")
my_otro_set.add("pepe")
print(my_otro_set)
print("buscar un elemento en un set")
print("Juan" in my_otro_set)
print("Luis" in my_otro_set)
print("eliminar dentro de un set")
my_otro_set.remove("Luis")
print(my_otro_set)
print("unir dos set")
my_tercer_set = my_set.union(my_otro_set)
print(my_set)
print(my_otro_set)
print(my_tercer_set)
print("buscar diferencias entre 2 set , en este caso omite pepe ")
print(my_otro_set.difference(my_set))