"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_calls = [x[0] for x in calls]
answering_calls = [x[1] for x in calls]

outgoing_texts = [x[0] for x in texts]
answering_texts = [x[1] for x in texts]

non_telemarketers = answering_calls+outgoing_texts+answering_texts

telemarketers = [x for x in outgoing_calls if x not in non_telemarketers]

unique_telemarkers={}
for telemarketer in telemarketers:
    if telemarketer not in unique_telemarkers:
        unique_telemarkers[telemarketer] = True
    else:
        continue

unique_telemarkers_lst = list(unique_telemarkers.keys())
unique_telemarkers_lst.sort()

print("These numbers could be telemarketers: ")
print('\n'.join(map(str, unique_telemarkers_lst)))
