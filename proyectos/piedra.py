import random

opciones = ['piedra', 'papel', 'tijeras']

while True:
    pcOpcion = random.choice(opciones)

    userOpcion = input("Piedra, papel o tijeras?: ")

    print('PC: ' + pcOpcion)
    print()


    if userOpcion == pcOpcion: 
        print('Empate!!!')

    elif userOpcion == 'piedra' and pcOpcion == 'papel':
        print('Papel gana a piedra: PC gana')

    elif userOpcion == 'piedra' and pcOpcion == 'tijeras':
        print('Piedra gana a tijeras: User gana!!!')

    elif userOpcion == 'papel' and pcOpcion == 'piedra':
        print('Papel gana a piedra: User gana!!!')

    elif userOpcion == 'papel' and pcOpcion == 'tijeras':
        print('Tijeras gana a papel: PC gana')

    elif userOpcion == 'tijeras' and pcOpcion == 'piedra':
        print('Piedra gana a tijeras: PC gana')

    elif userOpcion == 'tijeras' and pcOpcion == 'papel':
        print('Tijeras gana a papel: User gana!!!')

    print()
    print('Quiere seguir jugando?(S/N): ')
    respuesta = input()
    if respuesta == 'n':
        break