# Reading the Data...
days = int(input())

# Calculating the values...
years = int(days / 365)
days %= 365

months = int(days / 30)
days %= 30

print('{0} ano(s)\n{1} mes(es)\n{2} dia(s)'.format(years, months, days))
