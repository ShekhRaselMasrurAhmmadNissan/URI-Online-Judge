t = int(input())

array = list(map(int, input().split()))
number = array[0]
position = 0

for i in range(1, t):
    if (number >= array[i]):
        number = array[i]
        position = i
        
print(f'Menor valor: {number}\nPosicao: {position}')
