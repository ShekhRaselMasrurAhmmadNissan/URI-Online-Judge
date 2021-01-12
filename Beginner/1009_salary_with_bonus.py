# Reading the Data...
# sellers_name = input("employee's first name ")
sellers_name = input()
fixed_salary = float(input())
total_product_sale = float(input())

# Calculating Bonus...
bonus = float(total_product_sale * (15 / 100))

# Calculating Final Salary with Bonus...
final_salary = fixed_salary + bonus

# Printing the result...
print('TOTAL = R$ {0:.2f}'.format(final_salary))
