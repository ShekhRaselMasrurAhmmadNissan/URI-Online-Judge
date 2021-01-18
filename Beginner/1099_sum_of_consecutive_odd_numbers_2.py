# Reading the Data...
n = int(input())
results = list()
while True:
    if 
        for i in range(n):
            X, Y = map(int, input().split())

            if (X > Y):
                start_point = Y
                end_point = X
            else:
                start_point = X
                end_point = Y

            sum = 0

            for number in range(start_point + 1, end_point):
                if (number % 2 != 0):
                    sum += number

            results.append(sum)

        for result in results:
            print(result)
