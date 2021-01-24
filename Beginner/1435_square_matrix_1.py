while True:
    N = int(input())

    if (N == 0):
        break

    array =  []

    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(1)
        array.append(tmp)

    value = 1
    column = 0
    row = 0
    column_limit = N - 1
    row_limit = N - 1

    if (N % 2 == 0):
        layer = N / 2

    else:
        layer = (N + 1) / 2


    while (value <= layer):
        i = row
        while (i <= column_limit):
            array[column][i] = value
            array[row_limit][i] = value
            i+=1

        i = (column + 1)
        while ( i < row_limit):
            array[i][row] = value
            array[i][column_limit] = value
            i+=1

        value+=1
        column+=1
        row_limit-=1
        row+=1
        column_limit-=1

    for i in range(N):
        to_print = ''
        for j in range(N):
            to_print += " %3d" %array[i][j]
        print(to_print[1:])
    print("")
