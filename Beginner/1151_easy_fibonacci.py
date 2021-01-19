numbers = [0, 1]
x = int(input())
second_last = numbers[0]
last = numbers[1]
for i in range(2, x):
    sum = second_last + last
    second_last, last = last, sum
    numbers.append(sum)
result = ' '.join(map(str, numbers))
print(result)
