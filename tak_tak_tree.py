# Problema del tak tak tree, introduce la cantidad de frutos existentes
# y cuenta las noches para que alcance de forma equitativa(-1) entre 11 persona 
f = int(input(''))
frutos = 0
for noches in range(30):
    frutos = f*(2**noches)
    if (frutos-1) % 11 == 0:
        break
    else:
        frutos = 0
print(noches , frutos)

