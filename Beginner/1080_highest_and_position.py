# Reading the value...
highest = 0
position = 0
for i in range(100):
    number = int(input())
    if (number > highest):
        highest = number
        position = i + 1

print(f'{highest}\n{position}')
