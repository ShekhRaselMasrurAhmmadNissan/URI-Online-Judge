while True:

    number = int(input())

    if (number == 0):
        break

    array = []
    for i in range(1, (number + 1)):
        temp = []
        count = i
        for j in range(number):
            temp.append(abs(count))
            if (count == 1):
                count -= 3
            else:
                count -= 1
        array.append(temp)

    for i in range(number):
        to_print = ''
        for j in range(number):
            to_print += " %3d" %array[i][j]
        print(to_print[1:])
    print('')
