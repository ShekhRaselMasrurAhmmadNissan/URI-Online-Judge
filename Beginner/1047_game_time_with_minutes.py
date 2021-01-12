# Reading the Data...
start_time_hour, start_time_minute, end_time_hour, end_time_minute = map(
    int, input().split())

# Checking the conditions


# def check_minute(start_time_minute, end_time_minute, end_time_hour):
#     if (start_time_minute > end_time_minute):
#         end_time_minute += 60
#         end_time_hour -= 1
#     return end_time_minute, end_time_hour


# if (start_time_hour < end_time_hour):
#     end_time_minute, end_time_hour = check_minute(
#         start_time_minute, end_time_minute, end_time_hour)
#     duration_hour = end_time_hour - start_time_hour
#     duration_minute = end_time_minute - start_time_minute
# elif (start_time_hour > end_time_hour):
#     end_time_minute, end_time_hour = check_minute(
#         start_time_minute, end_time_minute, end_time_hour)
#     duration_hour = (24 - start_time_hour) + end_time_hour
#     duration_minute = end_time_minute - start_time_minute
# elif (start_time_hour == end_time_hour):
#     end_time_minute, end_time_hour = check_minute(
#         start_time_minute, end_time_minute, end_time_hour)
#     duration_hour = (24 - start_time_hour) + end_time_hour
#     duration_minute = end_time_minute - start_time_minute

difference = ((end_time_hour * 60) + end_time_minute) - \
    ((start_time_hour * 60) + start_time_minute)

if (difference <= 0):
    difference += 24 * 60

duration_hour = difference // 60
duration_minute = difference % 60

print(f'O JOGO DUROU {duration_hour} HORA(S) E {duration_minute} MINUTO(S)')
