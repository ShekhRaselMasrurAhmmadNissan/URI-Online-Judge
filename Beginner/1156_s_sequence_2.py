sum = 0
count = 1
for i in range(1, 40, 2):
    division = i / count
    sum += division
    count *= 2

print(f'{sum:0.2f}')
