saldo = 1000

print("\t .:MENÚ:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostra dinero disponible")
print("4. Salir")
opcion = int(input("Digite una opción del menú: "))

print()

if opcion == 1:
    extra = float(input("¿Cuanto dinero desea ingresar?: "))
    saldo += extra
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 2:
    retirar = floa(input("¿Cuanto dinero desea retirar?: "))
    if retirar > saldo:
        print("No tienes la cantidad suficiente de dinero")
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo}")
elif opcion == 3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 4:
    print("Gracias por utilizar nuestro cajero automático")
else:
    print("Se equivoco de opción de menú")


