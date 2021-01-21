n = int(input())

for i in range(n):
    number = int(input())
    sum = 0

    for x in range(1, number):
        if (number % x == 0):
            sum += x

    if (sum == number):
        print(f'{number} eh perfeito')
    else:
        print(f'{number} nao eh perfeito')
