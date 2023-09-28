#Importamos esta librería para poder facer o os.system('pause') e os.system('cls')
import os
       
#Pedimos 2 números e verificamos que o que entra non é unha cadena de texto
print("Dame 2 números para comenzar")
try:
    num1 = float(input('X='))
    num2 = float(input('Y='))
except ValueError:
    print('\nDebes escribir números, no strings\n')

print("""¿Qué operación desea hacer?
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Cambiar números
        6. Salir del programa
        """)

#Mentres !salir faremos un bucle infinito
salir = False
while salir == False:
    # Pedimos a opción que desexa facer con eses 2 números, tendo as posibilidades sempre arriba e
    # coas operacións amosadas xusto debaixo. Se se desexan cambiar os números borraranse os cálculos feitos
    # ata ese momento e introducirá outros valores.
    opcion = input('Opción: ')
    
    if(opcion == "6" or opcion.lower() == "salir"):
        salir = True
        print("Chaooo")
        exit() 

    if(opcion == "1" or opcion.lower() == "suma"):
        resultado = num2 + num1
        print(num1, "+", num2, "=", resultado)
    elif(opcion == "2" or opcion.lower() == "resta"):
        print(num1, "-", num2, "=", (num1-num2))
    elif(opcion == "3" or opcion.lower() == "multiplicación"):
        resultado = num1 * num2
        print(num1, "*", num2, "=", resultado)
    elif(opcion == "4" or opcion.lower() == "división"):
        if num2 == 0:
            print("No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(num1, "/", num2, "=", resultado)
    elif(opcion == "5" or opcion.lower() == "cambiar números"):
        os.system('pause')
        os.system('cls')
        try:
            num1 = float(input('X='))
            num2 = float(input('Y='))
        except ValueError:
            print('\nDebes escribir números, no strings\nSaliendo del programa... me da pereza hacer más bucles...\n')
        
        print("""
        ¿Qué operación desea hacer?
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Cambiar números
        6. Salir del programa
        """)
        if(opcion == "6" or opcion.lower() == "salir"):
            salir = True
            print("Chaooo\n")
            exit() 
    else:
        print('Esa opción no la tengo programada\n')
    