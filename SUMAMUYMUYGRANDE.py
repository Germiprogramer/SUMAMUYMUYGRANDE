from random import randint

numero_filas = int(input("elige numero de filas = "))
numero_columnas = int(input("elige numero de filas = "))

matriz = []
for i in range(numero_filas):
    matriz.append([])
    for j in range(numero_columnas):
        matriz[i].append(int(randint(0,100)))

suma = 0

for i in range(numero_filas):
    for j in range(numero_columnas):
        suma += matriz[i][j]
        suma = float(suma)

print(matriz)

print(suma)