# Ejercicio: Definir una lista de 1..1000 y determinen todos los numeros primos que aparecen
# entre el 1 y el 1000, y guardarlos en una lista llamada numeros_primos.

# Resolucion:

numeros = list(range(1, 1001))
numeros_primos = []

for numero in numeros:
    if numero > 1:  # Los números menores o iguales a 1 no son primos
        es_primo = True
        for i in range(2, int(numero**0.5) + 1):  # Verificamos divisores hasta la raíz cuadrada del número
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(numero)

print("Los números primos entre 1 y 1000 son:")
for primo in numeros_primos:
    print(primo, end=", ")
print("\nTotal de números primos encontrados:", len(numeros_primos))
# El resultado de este código es una lista de números primos entre 1 y 1000, junto con el total de números primos encontrados.