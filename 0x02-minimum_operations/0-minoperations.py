#!/usr/bin/python3

"""
    Determines the number of minmum operations given in n characters
"""


def minOperations(n):
    """
        Function that calculates the fewest number of operations
        needed to give a result of exactly n H chars in a file
        args: n: Number of chars to be displayed
        return: Number of min operations
    """

    chars_in_file = 1
    no_of_times_copied = 0
    counter = 0
    while chars_in_file < n:
        remainder = n - chars_in_file
        if (remainder % chars_in_file == 0):
            no_of_times_copied = chars_in_file
            chars_in_file += no_of_times_copied
            counter += 2
        else:
            chars_in_file += no_of_times_copied
            counter += 1
    return counter
