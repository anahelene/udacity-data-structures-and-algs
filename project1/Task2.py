"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
incoming_calls_duration = [[x[0], x[3]] for x in calls]
answering_calls_duration = [[x[1], x[3]] for x in calls]

calls_duration = incoming_calls_duration + answering_calls_duration

calls_dict = {}
max_duration=0

for i in range(len(calls_duration)):
    key = calls_duration[i][0]
    value = int(calls_duration[i][1])
    if key not in calls_dict:
        calls_dict[key]= 0
        calls_dict[key]= value
    else:
        calls_dict[key]+=value
    if max_duration < calls_dict[key]:
        max_duration = calls_dict[key]
        max_key = key

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_key, max_duration))
