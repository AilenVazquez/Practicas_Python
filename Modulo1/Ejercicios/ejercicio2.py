# Pide al usuario que ingrese un número decimal (float). 
# Convierte ese número a un entero y luego a una cadena 
# de texto. Muestra ambos resultados.

decimal = float(input("ingrese un numero decimal: "))
entero = int(decimal)
string = str(decimal)

print(f"entero: {entero} y string: {string}")
print(f"entero: {type(entero)} y string: {type(string)}")
