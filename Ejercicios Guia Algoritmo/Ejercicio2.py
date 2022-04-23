#2- Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C respectivamente.
#El algoritmo debe imprimir cual es el mayor y cuál es el menor.
#Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos.
#Presente un mensaje de alerta en caso de que se detecte la introducción de valores iguales."""

print("Bienvenido al programa que identifica cual número es el mayor y cual el menor entre 3 números diferentes entre sí")
nombre = input("Antes de comenzar, ingresa tu nombre: ")
while True:
    try:
        num1 = float(input(f"{nombre}, Ingresa el primer valor: "))
        num2 = float(input(f"{nombre}, Ingresa el segundo valor: "))
        num3 = float(input(f"{nombre}, Ingresa el tercer valor: "))

        if num1 == num2 and num2 == num3:
            print(f"{nombre}, los valores ingresados son iguales, favor de introducir números diferentes")
            num1 = float(input(f"{nombre}, Ingresa el primer valor: "))
            num2 = float(input(f"{nombre}, Ingresa el segundo valor: "))
            num3 = float(input(f"{nombre}, Ingresa el tercer valor: "))

        if num1 == num2 or num2 == num3 or num1 == num3:
            print(f"{nombre}, dos de los valores ingresados, son iguales, favor introducir números diferentes")
            num1 = float(input(f"{nombre}, Ingresa el primer valor: "))
            num2 = float(input(f"{nombre}, Ingresa el segundo valor: "))
            num3 = float(input(f"{nombre}, Ingresa el tercer valor: "))

        if num1 >= num2 and num1 >= num3:
                print(f"El {num1} es el mayor")

                if num2 <= num3:
                    print(f"El {num2} es el menor")
                else:
                    print(f"El {num3} es el menor")

        elif num2 >= num1 and num2 >= num3:
                print(f"El {num2} es el mayor")

                if num1 <= num3:
                    print(f"El {num1} es el menor")
                else:
                    print(f"El {num3} es el menor")

        elif num3 >= num1 and num3 >= num2:
                print(f"El {num3} es el mayor")

                if num1 <= num2:
                    print(f"El {num1} es el menor")
                else:
                    print(f"El {num2} es el menor")

        exit(True)

    except ValueError:
        print("Por favor, ingresa un valor númerico")