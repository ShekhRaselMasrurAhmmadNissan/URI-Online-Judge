operation = input()
sum = 0
count = 0

for i in range(12):
    for j in range(12):
        value = float(input())

        if ((i < j) and (11 - i) < j):
            sum += value
            count += 1

if (operation == 'S'):
    print(f'{sum:0.1f}')
elif(operation == 'M'):
    average = sum / count
    print(f'{average:0.1f}')
