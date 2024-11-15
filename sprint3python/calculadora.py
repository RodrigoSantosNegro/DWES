from operaciones import suma, resta, multiplicacion, division

def calculadora():
    print("Holi, vamoh a calcular")
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        print("\nSelecciona una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        opcion = input("Elige una opción (1-4): ")

        if opcion == "1":
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == "4":
            print(f"Resultado: {division(num1, num2)}")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
        if continuar == "n":
            print("¡Gracias por usar la calculadora!")
            break
        elif continuar != "s":
            print("Entrada no válida. Saliendo del programa.")
            break

if __name__ == "__main__":
    calculadora()