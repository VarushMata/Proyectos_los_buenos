N = int(input('Ingrese el numerador: '))
D = int(input('Ingrese el denominador: '))
M = N%D
R = N/D
if M == 0:
    print('El resultado es: ', R)
elif N < D:
    print('El resultado es: ', M, '/', D)
else:
    print ('El resultado es: ', int(R), M, '/', D)
