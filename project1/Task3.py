"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import logging
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#Part 1
bang_calls = [x[0] for x in calls if '(080)'== x[0][0:5]]
ans_calls = [x[1] for x in calls if x[0] in bang_calls]

code_dict={}
for number in ans_calls:
    if '(' == number[0]:
        code = number[1:4]
    elif ' ' == number[5]:
        code = number[0:4]
    elif number[0:3] == '140':
        code = '140'
    if code not in code_dict:
        code_dict[code]=True

code_values_lst=code_dict.keys()
code_values_lst.sort()

print('The numbers called by people in Bangalore have codes:')
print('\n'.join(map(str, code_values_lst)))

#Part 2
bang_ans_calls = [x[1] for x in calls if ('(080)'== x[0][0:5]) & ('(080)'== x[1][0:5])]
percentage = (float(len(bang_ans_calls))/float(len(bang_calls)) * 100.00)
rounded_percentage = round(percentage, 2)

print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(rounded_percentage))
