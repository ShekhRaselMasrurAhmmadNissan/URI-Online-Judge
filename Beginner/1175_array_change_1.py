array = []

for i in range(20):
    array.append(int(input()))

for i in range(10):
    array[i], array[19 - i] = array[19 - i], array[i]

for i in  range(20):
    print(f'N[{i}] = {array[i]}')
