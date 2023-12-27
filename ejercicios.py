
def fizzbuzz():
    for index in range(1, 101):
        print(index)
        if index %3 == 0 and index %5 == 0:
            print("fizzbuz")
        elif index %3 == 0:
            print("fizz")
        elif index %5 == 0:
            print("buzz")          
        else:
            print(index)
print("Imprimir multiplos de 3, de 5, y de (3 y de 5)")
fizzbuzz()

print("comparamos si 2 palabras son anagramas (las dos palabras contienen las mismas letras)")
def is_anagram(palabra_uno,palabra_dos):
    palabra_uno=palabra_uno.lower()
    palabra_dos=palabra_dos.lower()
    if palabra_uno == palabra_dos:
        print("Son iguales")
        return False
    return sorted(palabra_uno) == sorted(palabra_dos)  # esto devuelve True o False
print(is_anagram("amor","Roam"))

print("imprime 50 primeros numeros , sucesion de numeros en el que el sguiente es la suma de los 2 anteriores")
def fibonacci():
    prev = 0
    next = 1
    for numero in range(0,50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib
fibonacci()