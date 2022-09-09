import numpy as np
N = int(input('Ingrese el tamaño de los vectores: '))
A = np.zeros((1,N))
B = np.zeros((1,N))
resultado = 0
for i in range(N):
    if i==0:
        for j in range(N):
            print('Ingresa el valor de A en la posición', j + 1, ':')
            A[0,j] = int(input(''))
    print('Ingrese el valor de B en la posición', i + 1 , ':')
    B[0,i] = int(input(''))
for n in range(N):
    resultado += A[0,i] * B[0,i]

print('El producto punto es: ',resultado)