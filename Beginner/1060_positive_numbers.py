# Reading the Data...
numbers = list()
for serial_number in range(0, 6):
    numbers.append(float(input()))
# Checking the conditions...
positive_number_count = 0

for number in numbers:
    if (number >= 0):
        positive_number_count += 1

print(f'{positive_number_count} valores positivos')
