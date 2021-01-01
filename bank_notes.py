# Reading the Data...
N = int(input())

# Calculating the Quantity of the notes...

# For 100 dollar Notes...
notes_100 = N / 100.0
reminder = N % 100.0

# For 50 dollar Notes...

notes_50 = reminder / 50.0
reminder = reminder % 50.0

# For 20 dollar Notes...
notes_20 = reminder / 20.0
reminder = reminder % 20.0

# For 10 dollar Notes...
notes_10 = reminder / 10.0
reminder = reminder % 10.0

# For 5 dollar Notes...
notes_5 = reminder / 5.0
reminder = reminder % 5.0

# For 2 dollar Notes...
notes_2 = reminder / 2.0
reminder = reminder % 2.0

# For 1 dollar Notes...
notes_1 = reminder / 1.0
reminder = reminder % 1.0

# Printing the results...
print('{0}\n{1} nota(s) de R$ 100,00\n{2} nota(s) de R$ 50,00\n{3} nota(s) de R$ 20,00\n{4} nota(s) de R$ 10,00\n{5} nota(s) de R$ 5,00\n{6} nota(s) de R$ 2,00\n{7} nota(s) de R$ 1,00'.format(N, int(notes_100), int(
    notes_50), int(notes_20), int(notes_10), int(notes_5), int(notes_2), int(notes_1)))
