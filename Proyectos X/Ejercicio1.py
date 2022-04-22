#Ejercicio No: 1 Desarrolle un algoritmo que permita leer dos valores distintos,
#determinar cuál de los dos valores es el mayor y escribirlo.
"""nombre = input("Antes de comenzar, por favor introduce tu nombre: ")

num1 = float(input(f"{nombre}, digita el primer valor númerico: "))
num2 = float(input(f"{nombre}, digita el segundo valor númerico, diferente al primero: "))

while num1 == num2:
    if num1 == num2:
        print("Los valores ingresados son iguales, favor de introducir números diferentes")
        num1 = float(input(f"{nombre}, digita el primer valor númerico: "))
        num2 = float(input(f"{nombre}, digita el segundo valor númerico, diferente al primero: "))

if num1 > num2:
    print(f"El número {num1} es el mayor")
else:
    print(f"El número {num2} es el mayor")
"""


######3

#num1 = float(input("Ingrese el primer valor: "))
#num2 = float(input("Ingrese el segundo valor: "))
#num3 = float(input("Ingrese el tercer valor: "))

print("Bienvenido al programa que identifica cual número es el mayor")
nombre = input("Antes de comenzar, ingresa tu nombre: ")
while True:
    try:
        num1 = float(input(f"{nombre}, Ingresa el primer valor: "))
        num2 = float(input(f"{nombre}, Ingresa el segundo valor: "))
        num3 = float(input(f"{nombre}, Ingresa el tercer valor: "))

        if num1 == num2 and num2 == num3:
            print("Los valores ingresados son iguales, favor de introducir números diferentes")
            num1 = float(input(f"{nombre}, Ingresa el primer valor: "))
            num2 = float(input(f"{nombre}, Ingresa el segundo valor: "))
            num3 = float(input(f"{nombre}, Ingresa el tercer valor: "))

        if num1 == num2 or num2 == num3:
            print("Dos de los valores ingresados, son iguales, y corresponden al mayor, favor introducir números diferentes")
            num1 = float(input(f"{nombre}, Ingresa el primer valor: "))
            num2 = float(input(f"{nombre}, Ingresa el segundo valor: "))
            num3 = float(input(f"{nombre}, Ingresa el tercer valor: "))

        if num1 >= num2 and num1 >= num3:
                print(f"El {num1} es el mayor")
        elif num2 >= num1 and num2 >= num3:
                print(f"El {num2} es el mayor")
        elif num3 >= num1 and num3 >= num2:
                print(f"El {num3} es el mayor")

    except ValueError:
        print("Por favor, ingresa un valor númerico")










