

numero1=5
numero2=1
numero2="pepe"

try:   #marca todo lo que queremos que si salta un error, entre por except:
   print(numero1+numero2)
   print("No Error")
except:#Obligatorio si hay un try
   print("Error")
else: #si ejecuta si no se produce ninguna excepcion. Opcional
   print("todo fue bien, la ejecucion continua")
finally: #se ejecuta siempre. Opcional
   print("la ejecucion continua correctamente")

print("Controlar errores determinados")
try:   #marca todo lo que queremos que si salta un error, entre por except:
   print(numero1+numero2)
   print("No Error")
except TypeError:
   print("Error de tipo TypeError")
except ValueError:
   print("Error de tipo ValueError")

print("sacar la informacion del error:")
try:   #marca todo lo que queremos que si salta un error, entre por except:
   print(numero1+numero2)
   print("No Error")
except TypeError as var_mi_error:
   print("Error de tipo TypeError")
   print(var_mi_error)
except Exception as var_cualquier_otro_error:
   print("Cualquier error que no haya sido controlado de manera particular")
   print(var_cualquier_otro_error)
   