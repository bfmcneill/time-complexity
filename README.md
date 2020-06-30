# Phone call and text message analysis

- Create algorithm
- Analyze algorithm worst case time complexity

## `Task0.py`

    - Worse case complexity: O(1)
    - inputs: 2 sequential lists of communication data
    - output: extracted element from input data
    - Algorithm:
      - select the list element from communication data
      - interpolate extracted values into a printed message 

## `Task1.py`

    - Worse case complexity : O(n)
    - inputs: 2 sequential lists of communication data
    - output: unique telephone count for call communication types
    - Algorithm:
      - initialize an empty set 
      - add sender and receiver to the set, set takes care of duplicates
      - calculate the size of the set
      - interpolate set size value into a printed message  

## `Task2.py`

    - Worse case complexity : O(n)
    - inputs: 2 sequential lists of communication data
    - output: max cumulative call duration and the associated phone number
    - Algorithm for `iterate_calls`:
      - initialize an empty dictionary 
      - iterate over call data and unpack the caller, receiver, and duration
      - send caller and duration to helper function accumulator
      - send receiver and duration to helper function accumulator
      - sort the telephone dict
    - Algorithm for `increase_duration`:
      - test if the telephone key has a cumulative value
      - increment cumulative value with call duration if exists 
      - else create new record and set initial value to call duration

## `Task3.py`

    - Worse case complexity : O(n)
    - inputs: 2 sequential lists of communication data
    - output A: Unique list of number prefixes called from Bangalore
    - output B: Percent of calls that are Bangalore local
    - Algorithm for `iterate_calls`:
      - create helper function for determine if number is mobile
      - create helper function to determine if number is fixed
      - create helper function to determine if number is a Bangalore number
      - instantiate an empty set for collecting unique values
      - instantiate a container for count of mobile numbers
      - instantiate a container for count of fixed numbers
      - instantiate a container for count of Bangalore local calls
      - Iterate through call records and filter processing for only calls made from Bangalore
      - For each record run 3 tests:
        - determine if call was made to a mobile or fixed caller and increment the count for each respective call recipient type
        - determine if call was a local bangalore call and increment if local
      - print sorted unique number prefix list ascending
      - calculate total call recipient count (fixed and mobile)
      - determine the ratio of local received bangalore calls to total received calls
      - print the bangalore call ratio interpolated inside of a helpful message

## `Task4.py`

    - Worse case complexity : O(n)
    - inputs: 2 sequential lists of communication data
    - output: determine numbers likely to be telemarketers
    - Algorithm:
      - initialize four empty sets, each tracking outbound and inbound caller and texter
      - iterate calls and extract inbound / outbound phone numbers
      - iterate texts and extract inbound / outbound phone numbers
      - union all inbound callers and texter sets into one set
      - subtract all union values from the outbound list and capture remaining numbers
      - print each remaining number sorted ascending


## Resources for time complexity

- [Medium :: Algorithm Time Complexity and Big O Notation](https://medium.com/@StueyGK/algorithm-time-complexity-and-big-o-notation-51502e612b4d)
- [Khan Academy :: Big-O notation](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-o-notation)
- [HackerEarth :: Time and Space Complexity](https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/tutorial/)
- [Medium :: Understanding time complexity with Python examples](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)