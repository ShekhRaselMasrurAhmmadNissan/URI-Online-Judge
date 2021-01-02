# Reading the Data...
X, Y = map(int, input().split())

ITEM = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

# Printing the results...
print(f'Total: R$ {(ITEM[X]*Y):0.2f}')
