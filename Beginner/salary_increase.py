# Reading the Data...
salary = float(input())

# Checking the conditions
if (salary >= 0 and salary <= 400.00):
    increment = 15
    increased = salary * (increment / 100)
    increased_salary = salary + increased
elif (salary <= 800.00):
    increment = 12
    increased = salary * (increment / 100)
    increased_salary = salary + increased
elif (salary <= 1200.00):
    increment = 10
    increased = salary * (increment / 100)
    increased_salary = salary + increased
elif (salary <= 2000.00):
    increment = 7
    increased = salary * (increment / 100)
    increased_salary = salary + increased
elif (salary > 2000.00):
    increment = 4
    increased = salary * (increment / 100)
    increased_salary = salary + increased

print(
    f'Novo salario: {increased_salary:0.2f}\nReajuste ganho: {increased:0.2f}\nEm percentual: {increment} %')
