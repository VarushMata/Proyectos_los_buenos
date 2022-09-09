#Programa que recibe como entrada el peso de una sandía y muestra si se puede partir en números pares
kilos = int(input(''))
e1 = 0
e2 = 0
# if kilos % 2 == 0:
#     print('SI')
# else: 
#     print('NO')
for i in range(200):
    for u in range(200):
        if (i + u) == kilos and i % 2 == 0 and u % 2 == 0:
            e1 = i
            e2 = u
            break
    
if e1+e2 == kilos and e1 % 2 == 0 and e2 % 2 == 0:
    print('SI')
else:
    print('NO')
        