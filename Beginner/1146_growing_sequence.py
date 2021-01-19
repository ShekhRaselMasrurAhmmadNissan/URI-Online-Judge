numbers = []
while True:
    x = int(input())
    if (x == 0):
        break
    else:
        for number in range(1, x+ 1):
            numbers.append(number)
        result = ' '.join(map(str, numbers))
        print(result)
        numbers.clear()
