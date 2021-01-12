# Reading the Data...
date_input = map(input().split())
start_date=int
start_hour, start_minute, start_second = map(int, input().split(' : '))

end_date = int(input('Dia '))
end_hour, end_minute, end_second = map(int, input().split(' : '))

exact_start_time = start_second + \
    (start_minute * 60) + (start_hour * 3600) + (start_date * 24 * 3600)
exact_end_time = end_second + (end_minute * 60) + \
    (end_hour * 3600) + (end_date * 24 * 3600)

exact_duration = exact_end_time - exact_start_time

W = exact_duration // (24 * 3600)  # Days...
exact_duration %= (24 * 3600)

X = exact_duration // 3600  # Hours...
exact_duration %= 3600

Y = exact_duration // 60  # Minutes...

Z = exact_duration % 60  # Seconds...

print(f'{W} dia(s)\n{X} hora(s)\n{Y} minuto(s)\n{Z} segundo(s)')
