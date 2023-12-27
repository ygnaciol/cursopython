
print("Los mudulos con otros ficheros python , la nomenclatura de ese fichero no puede empezar por numeros")
print("podemos ejecutar cualquier cosa que este dentro del fichero importado")
import modulo
modulo.sum(5,10,1)
modulo.imprimir("pepe")
print("podemos cargar solo una parte del fichero del modulo a importar")
print("de esta manera al llamar a esa parte del fichero, no hay que hacer alusion al modulo")
print("directamente ponemos imprimirB('juan')en lugar de moduloB.imprimirB('Juan')")
from moduloB import imprimirB
imprimirB("Juan")
print("Hay ciertos modulos que son del sistema y pueden ser utiles")
print("Por ejemplo el modulo math para operaciones matematicas especiales")
import math
print(math.pi)
print(math.pow(2,8))