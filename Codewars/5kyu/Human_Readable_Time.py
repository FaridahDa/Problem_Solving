import datetime

#
# def make_readable():
#     # input is seconds and return in time format 00:00:00
#     # The maximum time never exceeds 359999 (99:59:59)
#     # need to take in the seconds
#     # convert it to human readable time format
#
#     datetime.datetime.fromtimestamp(
#         int(seconds)
#     ).strftime('%H:%M:%S')



time = datetime.datetime.utcfromtimestamp(int('359999')).strftime('%H:%M:%S')
print(time)