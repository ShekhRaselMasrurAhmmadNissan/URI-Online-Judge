t = int(input())
array = []
if (1000 % t == 0):
    times = 1000 // t
else:
    times = (1000 // t) + 1
place = 0
for i in range(times):
    for x in range(t):
        if (place == 1000):
            break
        else:
            array.append(x)
        place += 1
for i in range(len(array)):
    print(f'N[{i}] = {array[i]}')
