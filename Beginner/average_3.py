# Reading the Data...
first_number, second_number, third_number, fourth_number = map(
    float, input().split())

average = ((first_number * 2) + (second_number * 3) +
           (third_number * 4) + (fourth_number * 1)) / (2 + 3 + 4 + 1)
print(f'Media: {average:.1f}')
# Checking the condition and printing the results...
if (average < 5):
    print('Aluno reprovado.')
elif (average >= 7):
    print('Aluno aprovado.')
else:
    print('Aluno em exame.')
    second_chance_number = float(input())
    print(f'Nota do exame: {second_chance_number:.1f}')
    final_average = (average + second_chance_number) / 2.0
    if (final_average < 5):
        print(f'Aluno reprovado.\nMedia final: {final_average:.1f}')
    else:
        print(f'Aluno aprovado.\nMedia final: {final_average:.1f}')
