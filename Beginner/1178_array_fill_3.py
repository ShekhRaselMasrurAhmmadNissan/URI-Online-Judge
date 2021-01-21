t = float(input())
array = [t]
for i in range(1, 100):
    array.append(array[i - 1] / 2)

for i in range(len(array)):
    print(f'N[{i}] = {array[i]:0.4f}')
