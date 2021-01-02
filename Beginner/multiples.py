# Reading the Data...
a, b = map(int, input().split())

# Checking the condition...
if (a != 0 and b != 0 and (b % a == 0) or (a % b == 0)):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
