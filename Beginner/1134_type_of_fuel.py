alcohol, gasoline, diesel = 0, 0, 0

while True:
    fuel = int(input())

    if(fuel == 1):
        alcohol += 1
    elif (fuel == 2):
        gasoline += 1
    elif (fuel == 3):
        diesel += 1
    elif (fuel == 4):
        break

print(f'MUITO OBRIGADO\nAlcool: {alcohol}\nGasolina: {gasoline}\nDiesel: {diesel}')
