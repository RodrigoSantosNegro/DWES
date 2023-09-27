puntuacion = 0

print("""Adivina adivinanza...
      ¿Qué es rojo y te puedes comer?
      a) Un ladrillo
      b) Pintura azul
      c) Un plátano
      """)

opcion = input('Respuesta (a, b ó c): ')

if(opcion == 'a' or opcion == 'A' or opcion.lower == 'un ladrillo'):
    print("Respuesta correcta")
    puntuacion += 10

else:
    print("Nanai, te equivocaste amigo")
    puntuacion -= 5
    
print("""Adivina adivinanza...
      Vuelo de noche, duermo de día, ¿qué soy yo?
      a) Un búho
      b) Un universitario promedio
      c) La luna
      """)
    
opcion = input('Respuesta (a, b ó c): ')

if(opcion == 'c' or opcion == 'C' or opcion.lower == 'la luna'):
    print("Respuesta correcta")
    puntuacion += 10
else:
    print("La verdad es que todas tienen sentido, pero has fallado :(")
    puntuacion -= 5

print("""Adivina adivinanza...
      Adivinanza: Soy un lugar donde puedes encontrar tinta y papel. La gente viene a mí para aprender y leer.
       ¿Qué soy?
      a) Biblioteca
      b) Escuela
      c) Librería
      """)
    
opcion = input('Respuesta (a, b ó c): ')

if(opcion == 'a' or opcion == 'A' or opcion.lower == 'biblioteca'):
    print("Respuesta correcta")
    puntuacion += 10
else:
    print("*Sonido de incorrecto* :p")
    puntuacion -= 5

print("Tu puntuación final ha sido: ", puntuacion)