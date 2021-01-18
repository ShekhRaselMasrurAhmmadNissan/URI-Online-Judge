# Reading the Data...
n = int(input())

# user_inputs = []
results = list()
sum = 0
for i in range (n):
    first_value, second_value, third_value = map(float, input().split())
    average = (((first_value * 2.0) + (second_value * 3.0) + (third_value * 5.0)) / (2.0 + 3.0 + 5.0))
    results.append(average)

for result in (results):
    print(f'{result:0.1f}')
