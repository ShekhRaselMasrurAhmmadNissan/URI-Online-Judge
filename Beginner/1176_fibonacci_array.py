array = [0, 1]
for i in range(2, 61):
    array.append((array[i - 1] + array[i - 2]))

x = int(input())

for i in range(x):
    place = int(input())
    print(f'Fib({place}) = {array[place]}')
