number = int(input())
array = []
for i in range(10):
    array.append(number)
    number *= 2

for i in range(10):
    print(f'N[{i}] = {array[i]}')
