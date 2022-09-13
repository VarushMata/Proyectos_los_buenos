# Programa que calcula el área que abarcan dos rectángulos menos su intersección
# introduciendo dos líneas con x1, y1, x2, y2
cadena = str(input(''))
coord1 = cadena.split(' ')
rectangulo = str(input(''))
coord2 = rectangulo.split(' ')

X11 = int(coord1[0])
Y11 = int(coord1[1])
X12 = int(coord1[2])
Y12 = int(coord1[3])

X21 = int(coord2[0])
Y21 = int(coord2[1])
X22 = int(coord2[2])
Y22 = int(coord2[3])

WR1 = abs(X12 - X11)
HR1 = abs(Y12 - Y11)

WR2 = abs(X22 - X21)
HR2 = abs(Y22 - Y21)

CR1X = (X12 + X11)/2
CR1Y = (Y12 + Y11)/2

CR2X = (X22 + X21)/2
CR2Y = (Y22 + Y21)/2

if abs(CR2X - CR1X) <= (WR1/2 + WR2/2) and abs(CR2Y - CR1Y) <= (HR1/2 + HR2/2):
    XINT1 = max(X11, X21)
    YINT1 = max(Y11, Y21)
    XINT2 = min(X12, X22)
    YINT2 = min(Y12, Y22)
    INTER = abs(XINT2 - XINT1) * abs(YINT2 - YINT1)
else:
    INTER = 0

AR1 = WR1 * HR1

AR2 = WR2 * HR2

AT = AR1 + AR2 - INTER
print(AT)
