"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

unique_numbers = set()

for row in texts:
    unique_numbers.add(row[0])
    unique_numbers.add(row[1])

for row in calls:
    unique_numbers.add(row[0])
    unique_numbers.add(row[1])

msg = f"There are {len(unique_numbers)} different telephone numbers in the records."
print(msg)

# worst case big O(n)

