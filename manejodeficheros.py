print("trabajando con ficheros txt")
print("abrimos de lectura escritura, si no existe,lo crearia")
fichero= open("C:/datos/curso python/mi_fichero.txt", "r+")
print("todo el fichero")
print(fichero.read())
fichero.close()
fichero= open("C:/datos/curso python/mi_fichero.txt", "r+")
print("los 10 primeros caracteres")
print(fichero.read(10))
fichero.close()
print("linea a linea")
fichero= open("C:/datos/curso python/mi_fichero.txt", "r+")
print(fichero.readline())
print(fichero.readline())
fichero.close()
fichero= open("C:/datos/curso python/mi_fichero.txt", "r+")
print("bucle for para leer el fichero linea a linea")
for linea in fichero.readlines():
    print(linea)
fichero.close()
fichero= open("C:/datos/curso python/mi_fichero.txt", "a")
print("escribir en el fichero al final, abrimos el ficheo con a de añadir")
fichero.write("\nAunque tambien me gusta shellscripts")
fichero.close()
fichero= open("C:/datos/curso python/mi_fichero.txt", "r")
print(fichero.read())
fichero.close()

print("manejar un JSON")
import json
json_file =  open("C:/datos/curso python/mi_fichero.json", "w+")
json_test = {
    "nombre":"Ignacio",
    "Apellido":"Lorduy",
    "Edad":55,
     "languaje":["Python", "Vb", "C++"],
     "website":"https://moure.dev"
     }
print("lo grabamos y si ponemos indent lo indenta de varias maneras segun el numero de indent")
json.dump(json_test,json_file,indent=0)
json_file.close()

with open("C:/datos/curso python/mi_fichero.json") as mi_otro_fichero:
   for linea in mi_otro_fichero.readlines():
    print(linea)    

print ("Se puede manejar tambien csv,xlsx y xml")
import csv
import xml