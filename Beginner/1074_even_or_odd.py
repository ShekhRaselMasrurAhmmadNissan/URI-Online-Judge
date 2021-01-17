# Reading the Data...
N = int(input())

numbers = list()

for i in range (N):
    numbers.append(int(input()))

for number in numbers:
    # Checking the condition for Null...
    if (number == 0):
        print('NULL')
    else:
        # Checking the EVEN or ODD Condition...
        if (number % 2 ==0):
            if (number > 0):
                print('EVEN POSITIVE')
            else:
                print('EVEN NEGATIVE')
        else:
            if (number > 0):
                print('ODD POSITIVE')
            else:
                print('ODD NEGATIVE')
