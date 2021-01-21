x = int(input())
sum = 0
while (x != 0):
    count = 0
    while (count < 5):
        if (x % 2 == 0):
            sum += x
            count += 1
        x += 1
    print(sum)
    sum = 0
    x = int(input())
