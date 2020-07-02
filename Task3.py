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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
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

# "(080)" in caller

is_mobile = lambda call: True if " " in call[1] else False
is_fixed = lambda call: True if ")" in call[1] else False
is_bangalore = lambda line: True if "(080)" in line else False

extract_mobile_prefix = lambda call: call[1].split(" ")[0][:4]
extract_fixed_prefix = lambda call: call[1].split(")")[0][1:]

unique_phone_prefix = set()
mobile_count = 0
fixed_count = 0
bangalore_local_call_count = 0

for call in calls:

    if is_bangalore(call[0]):

        if is_mobile(call):
            mobile_count += 1
            unique_phone_prefix.add(extract_mobile_prefix(call))

        elif is_fixed(call):
            fixed_count += 1
            unique_phone_prefix.add(extract_fixed_prefix(call))

        if is_bangalore(call[1]):
            bangalore_local_call_count += 1

# Part A - Unique list of number prefixes called from Bangalore
print("The numbers called by people in Bangalore have codes:")
[print(item) for item in sorted(unique_phone_prefix)]

# Part B - Percent of calls that are local
total_call_count = fixed_count + mobile_count
bangalor_call_ratio = bangalore_local_call_count / total_call_count

print(
    f"""{bangalor_call_ratio * 100:.2f} percent of calls from fixed lines in Bangalore 
are calls to other fixed lines in Bangalore."""
)