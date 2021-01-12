# Reading the Data...
salary = float(input())

# Checking the conditions...
if (salary >= 0.00 and salary <= 2000.00):
    print('Isento')
elif (salary <= 3000.00):
    salary_in_second_level = salary - 2000.00
    taxes = salary_in_second_level * (8 / 100.00)
    print(f'R$ {taxes:0.2f}')
elif (salary <= 4500.00):
    salary_in_third_level = salary - 3000.00
    taxes_in_second_level = 1000.00 * (8 / 100.00)
    taxes = (salary_in_third_level * (18 / 100.00)) + taxes_in_second_level
    print(f'R$ {taxes:0.2f}')
else:
    salary_in_fourth_level = salary - 4500.00
    taxes_in_second_level = 1000.00 * (8 / 100.00)
    taxes_in_third_level = 1500.00 * (18 / 100.00)
    taxes = (salary_in_fourth_level * (28 / 100.00)) + \
        taxes_in_second_level + taxes_in_third_level
    print(f'R$ {taxes:0.2f}')
