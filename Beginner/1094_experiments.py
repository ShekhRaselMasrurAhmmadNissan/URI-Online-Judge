# Reading the Data...
number_of_experiments = int(input())

total = 0
coelho = 0
rato = 0
sapo = 0

for experiment in range (number_of_experiments):
    count, animal = map(str, input().split())
    total += int(count)

    if (animal == 'C'):
        coelho += int(count)
    elif (animal == 'R'):
        rato += int(count)
    elif (animal == 'S'):
        sapo += int(count)

percentage_of_coelho = (coelho * 100.0) / total
percentage_of_rato = (rato * 100.0) / total
percentage_of_sapo = (sapo * 100.0) / total

print(f'Total: {total} cobaias\nTotal de coelhos: {coelho}\nTotal de ratos: {rato}\nTotal de sapos: {sapo}\nPercentual de coelhos: {percentage_of_coelho:0.2f} %\nPercentual de ratos: {percentage_of_rato:0.2f} %\nPercentual de sapos: {percentage_of_sapo:0.2f} %')
