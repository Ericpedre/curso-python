import random


palabras = ['autobus', 'arbusto']

palabra = random.choice(palabras)

letras = list(palabra)
letrasAdivinadas = []
letrasUsadas = []
lineas = ''
vidas = 7

palabraActual = ''
for letra in letras:
    if letra in letrasAdivinadas:
        palabraActual += ' ' + letra
    else:
        palabraActual += ' -'

while True:

    letra = input('Ingrese una letra: ')
    if letra in letrasUsadas:
        pass
    else:
        letrasUsadas.append(letra)

    if letra in letras:
        letrasAdivinadas.append(letra)
    
    if letra in letras:
        pass
    else:
        vidas -= 1

    palabraActual = ''
    for letra in letras:
        if letra in letrasAdivinadas:
            palabraActual += ' ' + letra
        else:
            palabraActual += ' -'

    print('Letras usadas: ' + str(letrasUsadas))
    print('Palabra: ' + palabraActual)
    print('Te quedan: ' + str(vidas) + ' vidas')

    if vidas == 0:
        print('F, Has perdido :( ')
        break
        
    if '-' in palabraActual:
        pass
    else:
        print('Has ganado!!!')
        break
        
