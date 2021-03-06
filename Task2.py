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

telephones = {}


def increase_duration(telephone, duration, telephones=telephones):
    """Create or update a telephone cumulative duration"""
    if telephone in telephones.keys():
        telephones[telephone] += duration
    else:
        telephones[telephone] = duration


def iterate_calls():
    """Accumulate duration for each telephone line on a call"""
    for call in calls:

        caller, receiving, duration = (call[0], call[1], int(call[3]))

        increase_duration(caller, duration)
        increase_duration(receiving, duration)

    return sorted(telephones.items(), key=lambda x: x[1])


# the longest time spent by a number cumulatively
phone_number, duration = iterate_calls()[-1]


msg = f"{phone_number} spent the longest time, {duration} seconds, on the phone during September 2016."
print(msg)
