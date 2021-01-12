# Reading the Data...
numbers = list()
for serial_number in range(0, 5):
    numbers.append(float(input()))
# Checking the conditions...
even_number_count = 0

for number in numbers:
    if (number % 2 == 0):
        even_number_count += 1

print(f'{even_number_count} valores pares')
