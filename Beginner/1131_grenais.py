count, inter, gremio, draw = 0, 0, 0, 0

while True:
    inter_score, gremio_score = map(int, input().split())
    count += 1
    if (inter_score > gremio_score):
        inter += 1
    elif (inter_score < gremio_score):
        gremio +=1
    else:
        draw += 1

    print('Novo grenal (1-sim 2-nao)')
    choice = int(input(''))

    if choice == 2:
        break

print(f'{count} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{draw}')
if (inter > gremio):
    print('Inter venceu mais')
elif (inter < gremio):
    print('Gremio venceu mais')
else:
    print('Não houve vencedor')
