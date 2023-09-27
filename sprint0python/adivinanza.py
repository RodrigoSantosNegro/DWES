print("""Adivina adivinanza...
      ¿Qué es rojo y te puedes comer?
      a) Un ladrillo
      b) Pintura azul
      c)Un plátano
      """)

opcion = input('Respuesta (a, b ó c): ')

if(opcion == 'a' or opcion == 'A' or opcion == 'Un ladrillo'):
    print("Respuesta correcta")
else:
    print("Nanai, te equivocaste amigo")
    