cadena = str(input(''))
U = cadena.split(' ')
N = int(U[0])
D = int(U[1])
M = N%D
R = N/D
if M == 0:
    print(int(R))
elif N < D:
    print(M,'/',D,sep='')
else:
    # print(int(R),M,'/',D,sep='')
    print(int(R), end=' ')
    print(M, '/', D, sep='')
    
