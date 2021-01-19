count = int(input())
start_point = 1
joined_number = []
joined_string = ''
for i in range(count):
    for number in range(start_point, start_point + 3):
        joined_number.append(number)

    joined_number.append('PUM')
    joined_string = ' '.join(map(str, joined_number))
    print(joined_string)
    joined_number.clear()
    start_point += 4
