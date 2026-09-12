# Pide al usuario que ingrese el valor de la base y la altura 
# de un triángulo (float). Calcula el área del triángulo 
# utilizando la fórmula área = (base * altura) / 2 y 
# muestra el resultado.
# Entradas del usuario
base = float(input("Ingresa la base del triángulo: "))
altura = float(input("Ingresa la altura del triángulo: "))

# Cálculo del área
area = (base * altura) / 2

print(f"El área del triángulo es: {area}")