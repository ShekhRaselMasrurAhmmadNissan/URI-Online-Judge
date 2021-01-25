while True:
    try:
        number = int(input())

        default_print = number - 1
        array = []
        for i in range(number):
            temporary = []
            for j in range(number):
                if (j == default_print):
                    temporary.append(2)
                    default_print -= 1
                else:
                    if (i == j):
                        temporary.append(1)
                    else:
                        temporary.append(3)
            array.append(temporary)

        for i in range(number):
            to_print = ''
            for j in range(number):
                to_print += str(array[i][j])
            print(to_print)

    except EOFError:
        break
