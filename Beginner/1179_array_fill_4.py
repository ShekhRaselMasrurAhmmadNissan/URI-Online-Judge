evan = []
odd = []

for i in range(15):
    number = int(input())

    if (number % 2 == 0):
        evan.append(number)

        if (len(evan) == 5):
            for x in range(5):
                print(f'par[{x}] = {evan[x]}')
            evan.clear()

    else:
        odd.append(number)

        if (len(odd) == 5):
            for x in range(5):
                print(f'impar[{x}] = {odd[x]}')
            odd.clear()

for x in range(len(odd)):
    print(f'impar[{x}] = {odd[x]}')

for x in range(len(evan)):
    print(f'par[{x}] = {evan[x]}')
