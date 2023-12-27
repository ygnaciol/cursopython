

import re
mi_cadena="Esta es la leccion numero 7: Expresiones Regulares"
mi_otra_cadena="Esta no es la leccion numero 6: Manejo  de ficheros"
print("busca un patron en un string")
print("con match buscamos en una cadenaX la cadenaY, con math busca cadenas que comiencen por esa otra cadena, si esta en otro lugar no lo encuentra ")
print(re.match("Esta es", mi_cadena))
print(re.match("Esta es", mi_otra_cadena))
print(re.match("Expresiones", mi_cadena))  #no lo encuentra porque no esta al princiupio de la cadena

print("findall nos saca las repeticione de una cadena, en ese caso la letra a")
var_findall = re.findall("a",mi_cadena, re.I)
print(var_findall)

print("split quita la cadena indicada")
var_split =re.split("a",mi_cadena)
print(var_split)

print("sub sustituye una cadena por otra")
var_sub =re.sub("a","A",mi_cadena)
print(var_sub)

print("patrones")
vpatron=r'[Ll]eccion'
print(re.findall(vpatron,mi_cadena))

vpatron=r'[Ll]eccion|Expresiones'
print(re.findall(vpatron,mi_cadena))

vpatron=r'[0-9]'
print(re.findall(vpatron,mi_cadena))
print(re.search(vpatron,mi_cadena))

vpatron=r'\d'
print(re.findall(vpatron,mi_cadena))

vpatron=r'[l].'
print(re.findall(vpatron,mi_cadena))