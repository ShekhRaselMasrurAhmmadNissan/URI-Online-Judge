n = int(input())

for i in range(n):
    number = int(input())
    is_prime = 0
    for x in range(1, number):
        if (number % x == 0):
            is_prime += 1

    if (is_prime == 1):
        print(f'{number} eh primo')
    else:
        print(f'{number} nao eh primo')
