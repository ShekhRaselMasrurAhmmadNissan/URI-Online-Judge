# Reading the Data...
numbers = list()
for serial_number in range(0, 6):
    numbers.append(float(input()))
# Checking the conditions...
positive_number_count = 0
sum = 0

for number in numbers:
    if (number >= 0):
        positive_number_count += 1
        sum += number
average = (sum / positive_number_count)
print(f'{positive_number_count} valores positivos\n{average:0.1f}')
