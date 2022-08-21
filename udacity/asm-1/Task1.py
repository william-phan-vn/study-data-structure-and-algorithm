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
def synthesize_phone_numbers(records) -> list:
    phone_numbers = []
    for record in records:
        if record[0] not in phone_numbers:
            phone_numbers.append(record[0])
        if record[1] not in phone_numbers:
            phone_numbers.append(record[1])
    return phone_numbers


phone_numbers = synthesize_phone_numbers(texts)
phone_numbers.extend(synthesize_phone_numbers(calls))
print(f'There are {len(phone_numbers)} different telephone numbers in the records.')