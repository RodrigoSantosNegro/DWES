import random

#Variable numérica a que se lle sumará 10pts en caso de resposta correcta ou restaráselle 5pts en caso incorrecto
puntuacion = 0

lista = [1, 2, 3]
random = random.sample(lista, 2)
print(random)
if(random.__contains__(1)):
    print("""Adivina adivinanza...
        ¿Qué es rojo y te puedes comer?
        a) Un ladrillo
        b) Pintura azul
        c) Un plátano
        """)
    #Pedimos que introduza a resposta que cree correcta o usuario e verificamos que sexa correcta
    opcion = input('Respuesta (a, b ó c): ')

    if(opcion == 'a' or opcion == 'A' or opcion.lower() == 'un ladrillo'):
        print("Respuesta correcta")
        puntuacion += 10

    else:
        print("Nanai, te equivocaste amigo")
        puntuacion -= 5
if(random.__contains__(2)):   
    print("""Adivina adivinanza...
        Vuelo de noche, duermo de día, ¿qué soy yo?
        a) Un búho
        b) Un universitario promedio
        c) La luna
        """)
        
    opcion = input('Respuesta (a, b ó c): ')

    if(opcion == 'c' or opcion == 'C' or opcion.lower() == 'la luna'):
        print("Respuesta correcta")
        puntuacion += 10
    else:
        print("La verdad es que todas tienen sentido, pero has fallado :(")
        puntuacion -= 5
if(random.__contains__(3)): 
    print("""Adivina adivinanza...
        Adivinanza: Soy un lugar donde puedes encontrar tinta y papel. La gente viene a mí para aprender y leer.
        ¿Qué soy?
        a) Biblioteca
        b) Escuela
        c) Librería
        """)
        
    opcion = input('Respuesta (a, b ó c): ')

    if(opcion == 'a' or opcion == 'A' or opcion.lower() == 'biblioteca'):
        print("Respuesta correcta")
        puntuacion += 10
    else:
        print("*Sonido de incorrecto* :p")
        puntuacion -= 5

print("Tu puntuación final ha sido: ", puntuacion)