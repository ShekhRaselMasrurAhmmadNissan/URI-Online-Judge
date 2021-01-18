# choice = 1
# while True:
#     if choice == 1:
#         sum = 0
#         count = 0
#         if (count != 2):
#             score = float(input())
#             if (score >= 0) and (score <= 10):
#                 sum += score
#                 count += 1
#             else:
#                 print('nota invalida')
#
#         else:
#             media = sum / count
#             print(f'media = {media:0.2f}')
#             print('novo calculo (1-sim 2-nao)')
#             choice = int(input())
#
#     elif (choice == 2):
#         break
#     else:
#         print('novo calculo (1-sim 2-nao)')
#         choice = int(input())

#URI Online Judge | 1118 Várias Notas Com Validação
count = 0
count_2 = 0
while(count < 2):
  x = float(input())
  if(x < 0) or (x > 10):
    print('nota invalida')
  else:
    count_2 += x
    count += 1
cal = count_2 / 2
print('media = %.2f' %cal)
print('novo calculo (1-sim 2-nao)')
t = int(input(''))
while(t != 2) or (t == 1):
  if(t != 1):
    print('novo calculo (1-sim 2-nao)')
    t = int(input(''))
    continue
  elif(t == 1):
    count = 0
    count_2 = 0
    while(count < 2):
      x = float(input())
      if(x < 0) or (x > 10):
        print('nota invalida')
      else:
        count_2 += x
        count += 1
    cal = count_2 / 2
    print('media = %.2f' %cal)
    print('novo calculo (1-sim 2-nao)')
    t = int(input(''))
