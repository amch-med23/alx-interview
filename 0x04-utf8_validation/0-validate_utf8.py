#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ The main method
    Args:
            data (list[int]): a list of integers
    """
    expected_leading_bytes = 0

    # the bit patterns for UTF-8 encoding
    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    # Loop over each byte in the input data
    for byte in data:
        # initializing a mask, to check for leading 1's
        leading_one_mask = 1 << 7
        if expected_leading_bytes == 0:
            # the number of 1's in the current leading byte
            while leading_one_mask & byte:
                expected_leading_bytes += 1
                leading_one_mask = leading_one_mask >> 1

            # moveto the next byte
            if expected_leading_bytes == 0:
                continue

            # invalid sequence
            if expected_leading_bytes == 1 or\
                    expected_leading_bytes > 4:
                return False

        else:
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        expected_leading_bytes -= 1

    if expected_leading_bytes == 0:
        return True
    else:
        return False
