# Reading the data...
employees_number = int(input())
numbers_of_hours_worked = int(input())
amount_per_hour = float(input())

# Calculating the salary...
salary = numbers_of_hours_worked * amount_per_hour

# Printing the result...
print('NUMBER = %d' % employees_number)
print('SALARY = U$ %0.2f' % salary)
