# Reading the values..
x, y, z = map(int, input().split())
original_list = [x, y, z]
copied_list = original_list.copy()

# Sorting...
for number in range(len(original_list)):
    for check in range(number + 1, len(original_list)):
        if (original_list[number] > original_list[check]):
            temp = original_list[number]
            original_list[number] = original_list[check]
            original_list[check] = temp

# Printing the Sorted Sequence...
for number in range(len(original_list)):
    print(original_list[number])
print('')
# Printing the Main Sequence...
for number in range(len(copied_list)):
    print(copied_list[number])
