# if 1 == 2:
#     print('hola')
#     print('Como estas')
# elif 1 == 1:
#     print('hola2')
# elif 1 == 1:
#     print('hola3')


# 8 > 2
# 3 < 7
# 5 == 5
# 2 != 3




















password = input('Ingrese una contraseña: ')

if len(password) > 5:
    if password == 'paloma':
        print('Welcome!')
    else:
        print('contraseña incorrecta')
else:
    print('contraseña invalida')