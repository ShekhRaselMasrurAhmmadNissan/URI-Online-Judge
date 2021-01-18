j_start = 7
for i in range(1, 10):
    if (i % 2 != 0):
        for j in range(j_start, j_start - 3, -1):
            print(f'I={i} J={j}')
        j_start += 2
