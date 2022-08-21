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
def update_phone_numbers(phone_numbers: dict, number: str, duration: int):

    if phone_numbers.get(number) is None:
        phone_numbers.update({
                number: duration
            })
    else:
        phone_numbers[number] += duration

phone_numbers = {}
for record in calls:
    update_phone_numbers(phone_numbers, record[0], int(record[3]))
    update_phone_numbers(phone_numbers, record[1], int(record[3]))

# Find the phone number that spends the longest calling time
max_duration = 0
output_phone_number = None
for phone, duration in phone_numbers.items():
    if duration > max_duration:
        max_duration = duration
        output_phone_number = phone

print(f'{output_phone_number} spent the longest time, {max_duration} seconds, '
      'on the phone during September 2016.')
