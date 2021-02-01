""" Follows the work done on exceptions in the course: Core Python: Getting Started @
https://app.pluralsight.com/course-player?clipId=a8b1ac0f-c305-4505-a0d8-b40f4f858fcf """

# imports

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
    try:                                            # try raises exceptions
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)                             # convert string to integer
        print(f"Conversion succeeded! x = {x}")     # print on success
    # except KeyError:                                # except handles exceptions for KeyError, tokens are not in
    #                                                 # Digit_Map as in string_to_integer2
    #     print("Conversion failed!")                 # print on failure
    #     x = -1
    # except TypeError:                               # except handles exceptions for TypeError, when the tokens is a
    #                                                 # not a string as in string_to_integer3
    #     print("Conversion failed!")
    #     x = -1

    except(KeyError, TypeError):                      # combined the previous statements to create one simple statement.
        print("Conversion failed!")

    return x  # return the integer


# to see if we are able to convert a strings to an integers
string_to_integer1 = convert("one three three seven".split())
print(string_to_integer1)

# to see if we are able to convert some arbitrary string
string_to_integer2 = convert("around two grillion".split())
print(string_to_integer2)   # this causes a KeyError as the 'around' cant be converted to an integer, this is because
                            # there is no 'around' key in DIGIT_MAP

string_to_integer3 = convert(512)
print(string_to_integer3)   # this causes a TypeError as the value 512 is
                            # an integer and not a string as expected in the convert function