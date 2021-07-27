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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
calling_calls = [x[0] for x in calls]
answering_calls = [x[1] for x in calls]

calling_texts = [x[0] for x in texts]
answering_texts = [x[1] for x in texts]

numbers_in_records = calling_calls + answering_calls + calling_texts + answering_texts

count_unique_numbers = len(set(numbers_in_records))

print("There are {} different telephone numbers in the records.".format(count_unique_numbers))
