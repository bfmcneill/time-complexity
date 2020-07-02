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

outbound_callers = set()
inbound_callers = set()
outbound_texter = set()
inbound_texter = set()

for call in calls:
    outbound_callers.add(call[0])
    inbound_callers.add(call[1])


for text in texts:
    outbound_texter.add(text[0])
    inbound_texter.add(text[1])

# create a combined list of inbound callers, and send/receive texters
exclude = inbound_callers.union(outbound_texter).union(inbound_texter)

print("These numbers could be telemarketers: ")
[print(item) for item in sorted(outbound_callers.difference(exclude))]
