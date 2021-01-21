n = int(input())

for i in range(n):
    count = 0
    sum = 0
    x, y = map(int, input().split())

    while (count < y):
        if (x % 2 != 0):
            sum += x
            count += 1
        x += 1
    print(sum)
