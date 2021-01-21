array = []
for i in range(100):
    array.append(float(input()))
    if(array[i] <= 10):
        print(f'A[{i}] = {array[i]:0.1f}')

# for i in range(100):
#     if(array[i] <= 10):
#         print(f'A [{i}] = {array[i]:0.1f}')
