
print("Los diccionarios se crean por pares de valor....(Nombre=ignacio) , (Edad=55) , etc")
my_dic= dict()
my_otro_dic = {}
print("Una forma de crear un diccionario")
my_otro_dic={"Nombre":"Ignacio","Apellido":"Lorduy","Edad":55,1:"Python"}
print("Otra forma de crear un diccionario")
my_dic = {
"Nombre":"Ignacio",
"Apellido":"Lorduy",
"Edad":55,
"Lenguajes":{"Python","C++","Visual Basic"},
1:1.77
}
print(my_dic)
print(my_otro_dic)
print("imprimir Nombre")
print(my_dic["Nombre"])
my_dic["Nombre"]="Pedro"
print(my_dic["Nombre"])
print("añadir un campo al diccionario")
my_dic["Calle"]="Marcelo Usera"
print(my_dic)
print("Eliminar un elemento del diccionario")
del my_dic["Edad"]
print(my_dic)
print("Comprobar si algo esta en el diccionario,hay que buscar por el campo, no por el contenido")
print("Pedro" in my_dic)
print("Nombre" in my_dic)
print("----")
print(my_dic)
print("----")
print("ver los items (formato lista)")
print(my_dic.items())
print("ver todos los keys/claves")
print(my_dic.keys())
print("ver todos los values\valores")
print(my_dic.values())