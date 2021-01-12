# Reading the Data...
a, b, c = map(float, input().split())

# Checking the condition...
if (((a + b) > c) and ((b + c) > a) and ((c + a) > b)):
    perimeter = (a + b + c)
    print(f'Perimetro = {perimeter:0.1f}')
else:
    area = ((a + b) / 2.0) * c
    print(f'Area = {area:0.1f}')
