line = int(input())
operation = input()
sum = 0

for i in range(12):
    for j in range(12):
        value = float(input())

        if (line == i):
            sum += value

if (operation == 'S'):
    print(f'{sum:0.1f}')
elif(operation == 'M'):
    average = sum / 12.00
    print(f'{average:0.1f}')
