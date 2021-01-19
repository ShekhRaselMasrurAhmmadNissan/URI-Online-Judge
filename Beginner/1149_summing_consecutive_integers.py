numbers = list(map(int, input().split()))
number_to_be_sum = numbers[0]
for number in range(1, len(numbers)):
    if (numbers[number] > 0):
        time_to_sum = numbers[number]
        break
sum = 0
for number in range(number_to_be_sum, number_to_be_sum + time_to_sum):
    sum += number
print(sum)
