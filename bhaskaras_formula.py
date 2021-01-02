# The Formula:   x1 = (- b + sqrt(b**2 - 4ac)) / 2a
#                x2 = (- b - sqrt(b**2 - 4ac)) / 2a

import math
# Reading the Data...
a, b, c = map(float, input().split())

D = (b ** 2) - (4 * a * c)
# Checking the donditions and printing the results...
if (D >= 0 and a != 0):
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    # print('R1 = {0:.5f}\nR2 = {1:.5f}'.format(x1, x2))
    print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')
else:
    print('Impossivel calcular')
