
var ="Este es un string \n con salto de linea"
print(var)
var="Este es un string \t con tabulacion"
print(var)
var="\\tEste es un string \n con escapado, la primera barra \ escapa el \t que le sigue"
print(var)

print("FORMATEO")
name="Ignacio"
surname="Lorduy"
age=55
print("Formato con format, Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Formateo con prcentaje, Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Formateo con print(f) Mi nombre es {name} {surname} y mi edad es {age}")

print("DESEMPAQUETADO DE CARACTERES")
languaje="Python"
a,b,c,d,e,f = languaje
print(a)
print(c)

print("DIVISON CADENAS")
print("imprimir partes de la cadena")
languaje_slice=languaje[1:3]
print(languaje_slice)
languaje_slice=languaje[1:]
print(languaje_slice)
languaje_slice=languaje[-2]
print(languaje_slice)
reversed_languaje=languaje[ :: -1]
print(reversed_languaje)

print ("FUNCINES")
print("primera letra mayuscula. todo mayusculas,cuenta,pregunta si es numerico ")
print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.isnumeric())
print("pregunta si es toda la cadena mayusculas")
print("XXXaXX".isupper())
print("La cadena comienza por Py")
print(languaje.startswith("Py"))