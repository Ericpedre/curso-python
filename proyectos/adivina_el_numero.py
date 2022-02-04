import random

pcOption = random.randint(1, 10)

vidas = 3

while True:
    print('Ingrese un numero del 1 al 10')
    userOption = int(input())

    if pcOption == userOption:
        print('Has ganado!!! :)')
        break
    else:
        print('Intente de nuevo')
        vidas = vidas - 1
        print('Vidas restantes: ' + str(vidas))
    
    if vidas == 0:
        print('F, Se te han agotado las vidas: :(')
        break

