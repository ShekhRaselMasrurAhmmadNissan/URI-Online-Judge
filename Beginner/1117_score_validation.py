sum = 0
count = 0
while (count != 2):
    score = float(input())
    if (score >= 0) and (score <= 10):
        sum += score
        count += 1
    else:
        print('nota invalida')

media = sum / count
print(f'media = {media:0.2f}')
