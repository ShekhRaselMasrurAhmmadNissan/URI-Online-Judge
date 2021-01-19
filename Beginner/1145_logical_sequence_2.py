x, y = map(int, input().split())
numbers = []
start_point = 1
if (y % x == 0):
    loop = (y // x)
else:
    loop = (y // x) + 1

for i in range(loop):
    for number in range(start_point, start_point + x):
        if (number <= y):
            numbers.append(number)

    result = ' '.join(map(str, numbers))
    print(result)
    numbers.clear()
    start_point += x
