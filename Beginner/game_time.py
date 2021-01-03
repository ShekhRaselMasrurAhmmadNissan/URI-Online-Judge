# Reading the Data...
start_time, end_time = map(int, input().split())

# Checking the conditions...
if (start_time < end_time):
    game_duration = end_time - start_time
    print(f'O JOGO DUROU {game_duration} HORA(S)')
elif (start_time > end_time):
    game_duration = (24 - start_time) + end_time
    print(f'O JOGO DUROU {game_duration} HORA(S)')
elif (start_time == end_time):
    game_duration = start_time + (24 - end_time)
    print(f'O JOGO DUROU {game_duration} HORA(S)')
