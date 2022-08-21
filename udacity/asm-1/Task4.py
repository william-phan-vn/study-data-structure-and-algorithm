"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from time import sleep

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
possible_numbers = []
making_text_numbers = [record[0] for record in texts]
answering_text_numbers = [record[1] for record in texts]

making_call_numbers = [record[0] for record in calls]
answering_call_numbers = [record[1] for record in calls]

for number in making_call_numbers:
    if number not in making_text_numbers \
            and number not in answering_text_numbers \
            and number not in answering_call_numbers \
            and number not in possible_numbers:
        possible_numbers.append(number)

possible_numbers.sort()
print(f'These numbers could be telemarketers: ')
for number in possible_numbers:
    print(number)
