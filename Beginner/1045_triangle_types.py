# Reading the Data...
a, b, c = map(float, input().split())
# Sorting the sides...
sides_list = [a, b, c]

for side in range(len(sides_list)):
    for check in range(side + 1, len(sides_list)):
        if (sides_list[side] < sides_list[check]):
            temp = sides_list[side]
            sides_list[side] = sides_list[check]
            sides_list[check] = temp

a, b, c = sides_list[0], sides_list[1], sides_list[2]

# Determining the types of the Triangle...
if (a > 0 and b > 0 and c > 0 and ((a + b) > c) and ((b + c) > a) and ((c + a) > b)):
    if (a >= (b + c)):
        print('NAO FORMA TRIANGULO')

    if ((a ** 2) == ((b ** 2) + c ** 2)):
        print('TRIANGULO RETANGULO')
    elif ((a ** 2) > ((b ** 2) + c ** 2)):
        print('TRIANGULO OBTUSANGULO')
    elif ((a ** 2) < ((b ** 2) + c ** 2)):
        print('TRIANGULO ACUTANGULO')

    if (a == b and b == c):
        print('TRIANGULO EQUILATERO')

    if ((a == b and a != c) or (b == c and b != a) or (a == c and a != b)):
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
