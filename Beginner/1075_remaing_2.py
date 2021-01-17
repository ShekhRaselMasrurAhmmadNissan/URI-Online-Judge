#Reading the Data...
N = int(input())

for i in range(1, 10000):
    if((i - 2) % N == 0):
        print(i)
