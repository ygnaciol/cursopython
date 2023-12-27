
print("Las clases por buenas practicas se esciben con la primera letra de cada palabra en mayuscula, sin espacios ni guiones bajos")
class MiPersonavacia:
    pass  #esta es la manera de que se pueda ejecutar en vacio

print(MiPersonavacia)
class MiPersona:
    #el parametro self es siempre obligatorio, se refiere a si mismo
    #podemos poner valores por defecto, observa "valias"
    def __init__(self, vnombre, vapellido, valias = "SIN ALIAS"):  #constructor de clase
        self.nombre=vnombre
        self.apellido=vapellido        
        self.alias=valias
        self.nombreyapellido=f"{vnombre} {vapellido} *****{valias}*****"
    #puedo meter una llamada a una funcion dentro de una clase
    #le paso siempre el self de la clase
    def caminando(self):
         print(f"{self.nombreyapellido} esta caminando.....")

print("creamos una copia (instanciamos) de la clase y la llamamos var_mi_persona1, y la imprimimos")
var_mi_persona1=MiPersona("Ignacio","Lorduy","El lordu")
print("creamos una copia (instanciamos) de la clase y la llamamos var_mi_persona2, y la imprimimos")      
var_mi_persona2=MiPersona("Alicia","Alonso")

print(f"{var_mi_persona1.nombre}")
print(f"{var_mi_persona1.apellido}")
print(f"{var_mi_persona1.alias}")
print(f"{var_mi_persona2.nombre} {var_mi_persona2.apellido}")
print(f"{var_mi_persona1.nombreyapellido}")
print(f"{var_mi_persona2.nombreyapellido}")
print(f"{var_mi_persona2.alias}")
print("Llamamos a la funcion caminando, que esta dentro de la clase MiPersona")
var_mi_persona1.caminando()
var_mi_persona2.caminando()