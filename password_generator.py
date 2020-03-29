# !/usr/bin/env python
# coding: utf-8

import argparse
from secrets import randbelow
from string import ascii_letters, punctuation

def random_number():
    # generate a random integer beetween 0 & 9
    result = randbelow(10)
    return result
    
def random_char():
    # generate a random lowercase or uppercase car in latin alphabet
    chars = ascii_letters
    return chars[randbelow(len(chars))]

def random_special_char():
    # generate a random special char
    special_chars = punctuation
    return special_chars[randbelow(len(special_chars))]

def list_to_string(s):
    # convert list to string to print result
    string = ""
    for c in s:
        string += str(c)
    return string

def switch(case):
    switcher = {
        0: random_number,
        1: random_char,
        2: random_special_char
    }
    func = switcher.get(case)
    return func()

def main():
    # Configure Argparse & able to set password length
    parser = argparse.ArgumentParser()
    parser.add_argument( "-l", "--length" , help="set password length (default=12)", 
                        type=int, default=12)
    args = parser.parse_args()

    # Set password length
    if args.length < 12:
        print('for your security, minimum length is 12')
        pass_len = 12
    else:
        pass_len = args.length
    
    result = None

    i = 0
    result = []
    # randomize call to random generation functions for pass_len
    while i < pass_len:
        result.append(switch(randbelow(3)))
        i += 1

    print(list_to_string(result))

if __name__ == "__main__":
    main()