array = []
for i in range(10):
    array.append(int(input()))

for i in range(len(array)):
    if(array[i] <= 0):
        array[i] = 1

for i in range(len(array)):
    print(f'X[{i}] = {array[i]}')
