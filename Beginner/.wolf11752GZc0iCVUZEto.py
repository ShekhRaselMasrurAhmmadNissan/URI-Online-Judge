# Reading the Data...
numbers = list()
numbers_to_be_read = int(input())
numbers_in_range = 0
number_out_range = 0
for number in range(0, numbers_to_be_read):
    numbers.append(int(input()))

for number in numbers:
    if (number >= 10 and number <= 20):
        number_in_range += 1
    else:
        number_out_range += 1

print(f'{number_in_range} in')