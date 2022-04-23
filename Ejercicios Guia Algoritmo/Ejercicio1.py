#1- Se necesita obtener el promedio simple de un estudiante a partir de sus tres notas parciales.
while True:
    try:
        nombre = input("Antes de comenzar, ingresa tu nombre: ")
        notas = int(input("Ingrese la cantidad de notas a promediar: "))
        suma = 0
        i = 1
        while i <= notas:
            print(f"{nombre}, ingresa la nota {i}: ")
            nota = float(input())
            suma += nota
            i += 1

        promedio = suma / notas
        print(f"{nombre} el promedio de las {i - 1} notas es {promedio}")

    except ValueError:
        print(f"{nombre}, por favor, ingresa un valor númerico")



