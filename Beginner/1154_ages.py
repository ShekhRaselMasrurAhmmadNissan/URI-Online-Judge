age = int(input())
sum_of_age = 0
count = 0
while (age >= 0):
    sum_of_age += age
    count += 1
    age = int(input())

average = sum_of_age / count
print(f'{average:0.2f}')
