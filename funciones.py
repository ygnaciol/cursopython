
########################################################
def mi_funcion():
    print("Esto es una funcion con argumentos")

def sumar_2_valores(primer_valor,segundo_valor):
    print("Esto es una funcion con argumentos")
    print(primer_valor+segundo_valor)
def sumar_2_valores_con_retorno(primer_valor,segundo_valor):
    print("Esto es una funcion con argumentos y devolucion de valor")
    varf1=primer_valor+segundo_valor
    return varf1
def imprimir_nombre_y_apellido(nombre,apellido):
    print("Esto es una funcion con argumentos sin tener que entrar en orden" )
    print(f"{nombre};{apellido}")
def imprimir_nombre_y_apellido_con_valores_por_defecto(nombre,apellido,alias="XXXXX"):
    print("Esto es una funcion con argumentos y valores por defecto" )
    print(f"{nombre};{apellido};{alias}")
def imprimir_textos(*texto):
    print(texto)
def imprimir_textos2(*texto):
    print("Podemos observar que lo que realmente recibe es una tupla")
    print (type(texto))
    for elemento in texto:
        print(elemento.upper())
   ########################################################
print("LAS VARIABLES GENERALES NO LAS RECONOCEN LAS FUNCIONES Y A LA INVERSA")
mi_funcion()  #llamo a la funcion
var1=5
var2=10
sumar_2_valores(var1,var2)
var1="pepe"
var2="juan"
sumar_2_valores(var1,var2)
var1=50
var2=100
var3=sumar_2_valores_con_retorno(var1,var2)
print(var3)
imprimir_nombre_y_apellido(apellido="Lorduy",nombre="Ignacio")
var1="Ignacio"
var2="Lorduy"
var3="El lordu"
print("Llamo a la funcion con argumentos por defecto, pero relleno todos")
imprimir_nombre_y_apellido_con_valores_por_defecto(var1,var2,var3)
print("Llamo a la funcion con argumentos por defecto, pero relleno solo 2, el tercero lo rellena por defecto")
imprimir_nombre_y_apellido_con_valores_por_defecto(var1,var2)
print("Llamo a la funcion con un numero de argumentos indeterminados, utilizo el simbolo *")
imprimir_textos("aaaa","bbbb","ccccccc")
print("Llamo a la funcion con un numero de argumentos indeterminados, y le doy formato")
imprimir_textos2("aaaa","bbbb","ccccccc")