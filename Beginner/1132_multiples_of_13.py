start_point = int(input())
end_point = int(input())
if (start_point > end_point):
    start_point, end_point = end_point, start_point
sum = 0
for number in range(start_point, end_point + 1):
    if (number % 13 != 0):
        sum += number

print(sum)
