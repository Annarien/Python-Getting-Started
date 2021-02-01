""" Follows the work done on exceptions in the course: Core Python: Getting Started @
https://app.pluralsight.com/course-player?clipId=a8b1ac0f-c305-4505-a0d8-b40f4f858fcf """

# imports
import sys
from math import log

# this is the DIGIT_MAP used throughout this file
DIGIT_MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


# defining a function
def convert(s):
    ''' Convert sting to integer'''
    # using try and except blocks to overcome KeyErrors when the token is not available in DIGIT_MAP
    x = -1
    try:  # try raises exceptions
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except(KeyError, TypeError) as e:  # e is a keyword
        print(f"Conversion error:{e!r}", file=sys.stderr)  # print standard error message
        raise  # re-raise the exception
        return -1


def string_log(s):
    v = convert(s)  # calls convert() function
    return log(v)  # computes natural log


# converting strings to logs
string_log1 = string_log("ouch!".split())  # this raises a ValueError: math domain error
string_log2 = string_log("cat dog".split())  # this raises a ValueError: math domain error
string_log3 = string_log(87452874561)  # this raises a ValueError: math domain error
