# Dada la edad de tres personas, edad1, edad2 y edad3, verifica si las tres edades son iguales. 
# Muestra el resultado de la comparación.

edad1 = int(input("Ingrese primer edad: "))
edad2 = int(input("Ingrese segunda edad: "))
edad3 = int(input("Ingrese tercer edad: "))

#----------------1----------------------

# if edad1 > edad2:
#     if edad1 > edad3:
#         if edad2 > edad3:
#             print(f"{edad1} es mayor que {edad2} y {edad2} es mayor que {edad3}")
#         else:
#             print(f"{edad1} es mayor que {edad2} y {edad3} es mayor que {edad2}")
#     else:
#         print(f"{edad3} es mayor que {edad1} y {edad1} es mayor que {edad2}")
# else:
#     if edad2 > edad3:
#         print(f"{edad1} es mayor que {edad2} y {edad2} es mayor que {edad3}")
#     else:
#         print(f"{edad1} es mayor que {edad2} y {edad3} es mayor que {edad2}")

#----------------2----------------------

# mayor = max(edad1, edad2, edad3)
# print(f"El mayor es {mayor}")

# menor = min(edad1, edad2, edad3)
# print(f"El menor es {menor}")


# if edad1 == edad2 == edad3:
#     print(f"Las 3 edades son iguales")
# else:
#     mayor = max(edad1, edad2, edad3)
#     menor = min(edad1, edad2, edad3)
#     if edad1 != mayor and edad1 != menor:
#         print(f"El mayor es: {mayor}")

numeros = []

numeros.append(edad1)
numeros.append(edad2)
numeros.append(edad3)

numeros.sort()

print(f"La edad menor es {numeros[0]}, la del medio es {numeros[1]} y la mayor {numeros[2]}")
            
#----------------1----------------------    

# if edad1 == edad2:
#     if edad1 == edad3:
#         print(f"Las 3 edades son iguales")
#     else:
#         print(f"La edad 1 y 2 son iguales pero la edad 3 es distinta")
# else:
#     if edad2 == edad3:
#         print(f"La edad 2 y 3 son iguales pero la edad 1 es distinta")
#     else:
#         if edad1 == edad3:
#             print(f"La edad 1 y 3 son iguales pero la edad 2 es distinta")
#         else:
#             print(f"Todas las edades sons distitnas")

#----------------2----------------------

# if edad1 == edad2 and edad1 == edad3:
#     print("Los tres numeros son iguales")
# else:
#     print("Son diferentes")























# edad1 = 25
# edad2 = 25
# edad3 = 25
# resultado = edad1 == edad2 == edad3
# print(resultado)  # True si las tres edades son iguales, de lo contrario False