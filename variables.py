
my_string_var ="My string variable"
print(my_string_var)

my_int_var = 5
print(my_int_var)
print ("aqui estamos creando una nueva variable que es string pariendo de una variable numerica, se hace con la funcion str()")
my_int_to_str_variable = str(my_int_var)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_boll_var = False
print(my_boll_var)
print("imprimo 3 variables de seguido en una misma linea: ",my_string_var,",",my_int_var,",",my_boll_var)
print("lalongitud de esta variable es :",len(my_string_var))

print ("poner en una linea valor a varias variable")
name,surname,alias,age="Ignacio","Lorduy","Lordu",35
print(name,surname,alias,age)
apellido=input("Cual es tu apellido: ")
print("tu apellido es:", apellido)