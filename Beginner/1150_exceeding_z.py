x = int(input())
while True:
    z = int(input())
    if (z > x):
        break

sum = 0
count = 0
for number in range(x, z + 1):
    sum += number
    count += 1

    if (sum > z):
        break

print(count)
