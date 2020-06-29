"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(
        reader
    )  # {sending number}, {receiving number}, {timestamp of text message}

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(
        reader
    )  # {calling number}, {receiving number}, {start timestamp of call}, {duration of call}

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

caller_max = ""
duration_max = -1

for call in calls:
    caller, duration = (call[0], int(call[3]))
    if duration > duration_max:
        caller_max = caller
        duration_max = duration

msg = f"{caller_max} spent the longest time, {duration_max} seconds, on the phone during September 2016."
print(msg)


# worst case big O(n)
