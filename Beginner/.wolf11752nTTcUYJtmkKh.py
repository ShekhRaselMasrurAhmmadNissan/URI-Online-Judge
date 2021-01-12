#Reading the Data...
start_point = int(input())

odd_number_count = 0

while True:
    if (start_point % 2 != 0):
        print(start_point)
        odd_number_count += 1
    
    if (odd_number_count == 6):
        b