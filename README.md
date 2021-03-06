# Phone call and text message analysis

- Create algorithm
- Analyze algorithm worst case time complexity

## `Task0.py`

    - Worse case complexity: `O(1)`
    - inputs: 2 sequential lists of communication data
    - output: extracted element from input data
    - Algorithm:
      - select the list element list `O(1)`
      - print message with interpolated variables `O(1)`

## `Task1.py`

    - Worse case complexity : `O(n)`
    - inputs: 2 sequential lists of communication data
    - output: unique telephone count for call communication types
    - Algorithm:
      - initialize an empty set `O(1)`
      - loop over a rows in a csv of texts `O(n)`
        - add each texter to set `O(1)`
      - loop over rows in a csv of callers `O(n)`
        - add each caller to to set `O(1)`
      - calculate the size of the set `O(1)`
      - print message with interpolated variables `O(1)`

## `Task2.py`

    - Worse case complexity : `(n log n)`
    - inputs: 2 sequential lists of communication data
    - output: max cumulative call duration and the associated phone number
    - Algorithm for `iterate_calls`:
      - initialize an empty dictionary `O(1)`
      - iterate over call data `O(n)`
        - unpack the caller, receiver, and duration for each row `O(1)`
          - increment caller duration `O(1)`
          - increment receiver duration `O(1)`
      - sort items `(n log n)`

## `Task3.py`

    - Worse case complexity : `O(n log n)`
    - inputs: 2 sequential lists of communication data
    - output A: Unique list of number prefixes called from Bangalore
    - output B: Percent of calls that are Bangalore local
    - Algorithm for `iterate_calls`:
      - create helper function for determine if number is mobile `O(1)`
      - create helper function to determine if number is fixed `O(1)`
      - create helper function to determine if number is a Bangalore number `O(1)`
      - instantiate an empty set for collecting unique values `O(1)`
      - instantiate a container for count of mobile numbers `O(1)`
      - instantiate a container for count of fixed numbers `O(1)`
      - instantiate a container for count of Bangalore local calls `O(1)`
      - Iterate through call records and filter processing for only calls made from Bangalore `O(n)`
      - loop over each record `O(n)`
        - determine if call was made to a mobile or fixed caller `O(1)`        
        - determine if call was a local bangalore call and increment if local `O(1)`
      - print sorted unique number prefix list ascending `O(n log n)`
      - calculate total call recipient count (fixed and mobile) `O(1)`
      - determine the ratio of local received bangalore calls to total received calls `O(1)`
      - print the bangalore call ratio interpolated inside of a helpful message `O(1)`

## `Task4.py`

    - Worse case complexity : `O(n log n)`
    - inputs: 2 sequential lists of communication data
    - output: determine numbers likely to be telemarketers
    - Algorithm:
      - initialize four empty sets `O(1)`
      - iterate calls `O(n)`
        - add data to set  `O(1)`
      - iterate texts `O(n)` 
        - add data to set  `O(1)`
      - union all inbound callers and texter sets into one set `O(n)`
      - subtract all union values from the outbound list and capture remaining numbers `O(n)`
      - sort the remaining values `O(n log n)`
      - print each remaining number sorted ascending `O(n)`


## Resources for time complexity

- [Medium :: Algorithm Time Complexity and Big O Notation](https://medium.com/@StueyGK/algorithm-time-complexity-and-big-o-notation-51502e612b4d)
- [Khan Academy :: Big-O notation](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-o-notation)
- [HackerEarth :: Time and Space Complexity](https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/tutorial/)
- [Medium :: Understanding time complexity with Python examples](https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7)
- [Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
- [Introduction to Big O Notation and Time Complexity](https://www.youtube.com/watch?v=D6xkbGLQesk)
- [Python Wiki :: Time Complexity](https://wiki.python.org/moin/TimeComplexity)