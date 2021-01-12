# Reading the Data...
sample = float(input())

# Checking the condition and printing the results...
if (sample >= 0 and sample <= 25):
    print('Intervalo [0,25]')
elif (sample > 25 and sample <= 50):
    print('Intervalo (25,50]')
elif (sample > 50 and sample <= 75):
    print('Intervalo (50,75]')
elif (sample > 75 and sample <= 100):
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
