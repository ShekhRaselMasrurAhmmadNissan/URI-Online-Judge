cases = int(input())

for i in range(cases):
    x, y = map(int, input().split())

    if (y == 0):
        print('divisao impossivel')
    else:
        result = x / y
        print(f'{result:0.1f}')
