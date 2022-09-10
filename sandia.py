#Programa que recibe como entrada el peso de una sandía y muestra si se puede partir en números pares
kilos = int(input(''))
if kilos == 2 or kilos == 1 or kilos == 0:
    print('NO')
else:
    if kilos % 2 == 0:
        print('SI')
    else:
        print('NO') 