numbers = list()
for serial_number in range(0, 5):
    numbers.append(int(input()))

even_number_count = 0
odd_number_count = 0
positive_number_count = 0
negative_number_count = 0

# Checking the conditions...
for number in numbers:
    # Even Odd
    if (number % 2 == 0):
        even_number_count += 1
    else:
        odd_number_count += 1

    if (number > 0):
        positive_number_count += 1
    elif(number < 0):
        negative_number_count += 1

print(f'{even_number_count} valor(es) par(es)\n{odd_number_count} valor(es) impar(es)\n{positive_number_count} valor(es) positivo(s)\n{negative_number_count} valor(es) negativo(s)')
