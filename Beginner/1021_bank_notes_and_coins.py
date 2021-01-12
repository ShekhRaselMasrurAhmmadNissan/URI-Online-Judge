# # Reading the Data...
# N = float(input())

# # Calculating the Quantity of the notes...

# # For 100 dollar Notes...
# dollar_100 = N / 100.0
# reminder = N % 100.0

# # For 50 dollar Notes...

# dollar_50 = reminder / 50.0
# reminder = reminder % 50.0

# # For 20 dollar Notes...
# dollar_20 = reminder / 20.0
# reminder = reminder % 20.0

# # For 10 dollar Notes...
# dollar_10 = reminder / 10.0
# reminder = reminder % 10.0

# # For 5 dollar Notes...
# dollar_5 = reminder / 5.0
# reminder = reminder % 5.0

# # For 2 dollar Notes...
# dollar_2 = reminder / 2.0
# reminder = reminder % 2.0

# # For 1 dollar coins...
# dollar_1 = reminder / 1.00
# reminder = reminder % 1.00

# # For 50 cents coins...
# coins_50 = reminder / 0.50
# reminder = reminder % 0.50

# # For 25 cents coins...
# coins_25 = reminder / 0.25
# reminder = reminder % 0.25

# # For 10 cents coins...
# coins_10 = reminder / 0.10
# reminder = reminder % 0.10

# # For 5 cents coins...
# coins_5 = reminder / 0.05
# reminder = reminder % 0.05

# # For 1 cents coins...
# coins_1 = reminder / 0.01
# reminder = reminder % 0.01
# Printing the results...
# print('NOTAS:\n{0} nota(s) de R$ 100.00\n{1} nota(s) de R$ 50.00\n{2} nota(s) de R$ 20.00\n{3} nota(s) de R$ 10.00\n{4} nota(s) de R$ 5.00\n{5} nota(s) de R$ 2.00\nMOEDAS:\n{6} moeda(s) de R$ 1.00\n{7} moeda(s) de R$ 0.50\n{8} moeda(s) de R$ 0.25\n{9} moeda(s) de R$ 0.10\n{10} moeda(s) de R$ 0.05\n{11} moeda(s) de R$ 0.01'.format(int(dollar_100), int(
#     dollar_50), int(dollar_20), int(dollar_10), int(dollar_5), int(dollar_2), int(dollar_1), int(
#     coins_50), int(coins_25), int(coins_10), int(coins_5), int(coins_1)))


# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------

value = eval(input())

cem = cinquenta = vinte = dez = cinco = dois = um = 0
cincents = vintecincents = dezcents = cincocents = cents = 0

value = float("%.2f" % value)
if int(value/100) >= 1:
    cem = int(value/100)
    value -= cem*100

value = float("%.2f" % value)
if int(value/50) >= 1:
    cinquenta = int(value/50)
    value -= cinquenta*50

value = float("%.2f" % value)
if int(value/20) >= 1:
    vinte = int(value/20.00)
    value -= vinte*20

value = float("%.2f" % value)
if int(value/10) >= 1:
    dez = int(value/10)
    value -= dez*10.00

value = float("%.2f" % value)
if int(value/5) >= 1:
    cinco = int(value/5)
    value -= cinco*5

value = float("%.2f" % value)
if int(value/2) >= 1:
    dois = int(value/2)
    value -= dois*2

value = float("%.2f" % value)
if int(value/1) >= 1:
    um = int(value/1)
    value -= um*1

value = float("%.2f" % value)
if int(value/0.50) >= 1:
    cincents = int(value/0.50)
    value -= cincents*0.50

value = float("%.2f" % value)
if int(value/0.25) >= 1:
    vintecincents = int(value/0.25)
    value -= vintecincents*0.25

value = float("%.2f" % value)
if int(value/0.10) >= 1:
    dezcents = int(value/0.10)
    value -= dezcents*0.10

value = float("%.2f" % value)
if int(value/0.05) >= 1:
    cincocents = int(value/0.05)
    value -= cincocents*0.05

value = float("%.2f" % value)
if int(value/0.01) >= 0.998:
    cents = int(value/0.01)
    value -= cents*0.01

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % cem)
print("%d nota(s) de R$ 50.00" % cinquenta)
print("%d nota(s) de R$ 20.00" % vinte)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinco)
print("%d nota(s) de R$ 2.00" % dois)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % um)
print("%d moeda(s) de R$ 0.50" % cincents)
print("%d moeda(s) de R$ 0.25" % vintecincents)
print("%d moeda(s) de R$ 0.10" % dezcents)
print("%d moeda(s) de R$ 0.05" % cincocents)
print("%d moeda(s) de R$ 0.01" % cents)
