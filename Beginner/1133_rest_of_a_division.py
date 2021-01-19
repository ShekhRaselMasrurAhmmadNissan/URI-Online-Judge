start_point = int(input())
end_point = int(input())

if (start_point > end_point):
    start_point, end_point = end_point, start_point

for number in range(start_point + 1, end_point):
    if ((number % 5 == 2) or (number % 5 == 3)):
        print(number)
