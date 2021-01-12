# # Reading the Data...
# start_date = int(input('Dia '))
# start_hour, start_minute, start_second = map(int, input().split(' : '))

# end_date = int(input('Dia '))
# end_hour, end_minute, end_second = map(int, input().split(' : '))

# exact_start_time = start_second + \
#     (start_minute * 60) + (start_hour * 3600) + (start_date * 24 * 3600)
# exact_end_time = end_second + (end_minute * 60) + \
#     (end_hour * 3600) + (end_date * 24 * 3600)

# exact_duration = exact_end_time - exact_start_time

# W = exact_duration // (24 * 3600)  # Days...
# exact_duration %= (24 * 3600)

# X = exact_duration // 3600  # Hours...
# exact_duration %= 3600

# Y = exact_duration // 60  # Minutes...

# Z = exact_duration % 60  # Seconds...

# print(f'{W} dia(s)\n{X} hora(s)\n{Y} minuto(s)\n{Z} segundo(s)')


valor = input().split()
d1 = int(valor[1])

valores = input().split(" : ")
h1,m1,s1 = list(map(int,valores))


valor = input().split()
d2 = int(valor[1])

valores = input().split(" : ")
h2,m2,s2 = list(map(int,valores))

d = d2 - d1

h = h2 - h1
if(h < 0):
    h = 24 + h
    d = d - 1

m = m2 - m1 
if(m < 0):
    m = 60 + m
    h = h - 1

s = s2 - s1
if(s < 0):
    s = 60 + s
    m = m - 1

if(d <= 0):
    d = 0

print("%d dia(s)" %d)
print("%d hora(s)" %h)
print("%d minuto(s)" %m)
print("%d segundo(s)" %s)