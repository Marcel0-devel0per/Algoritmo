import math

cateto1 = int(input("Introduce el valor númerico del cateto 1: "))
cateto2 = int(input("Introduce el valor númerico del cateto 2: "))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"El valor de la longitud de la hipotenusa es: {hipotenusa}")