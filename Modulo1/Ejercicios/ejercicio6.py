# Escribe un programa que convierta una cantidad en metros a otras unidades (centímetros, milímetros, pulgadas). 
# Pide al usuario que ingrese la cantidad en metros y realiza las conversiones utilizando operadores aritméticos. 

# pulgadas = metros * 39.3701

metros = float(input("Ingrese cantidad de metros: "))
pulgadas = metros * 39.3701
centimetros = metros * 100
milimetros = metros * 1000

print(f"Centimetros: {centimetros}")
print(f"Milimetros: {milimetros}")
print(f"Pulgadas: {pulgadas}")