nombre = input("Antes de comenzar, indicame tu nombre: ")
print(f"{nombre}, por favor, indicame dos números diferentes entre ellos.")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

while num1 == num2:
    if num1 == num2:
        print("Los números son iguales, por favor, ingresa números diferentes.")
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El número {num2}, es el menor.")

else:
    print(f"El número {num1}, es el menor.")

