X = int(input())
Y = int(input())

if (X > Y):
    start_point = Y
    end_point = X
else:
    start_point = X
    end_point = Y

sum = 0

for number in range(start_point + 1, end_point):
    if (number % 2 != 0):
        sum += number

print(s)