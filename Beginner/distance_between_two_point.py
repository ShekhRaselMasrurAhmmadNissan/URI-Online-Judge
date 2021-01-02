import math

# Reading the points...
x1, y1 = input().split(' ')
x2, y2 = input().split(' ')

# Calculating the distance...
distance = math.sqrt(((float(x2) - float(x1)) ** 2) +
                     ((float(y2) - float(y1)) ** 2))
# Printing the result...
print('{0:.4f}'.format(distance))
