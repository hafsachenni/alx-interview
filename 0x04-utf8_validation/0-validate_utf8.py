#!/usr/bin/python3
"""utf-8 validation task"""


def validUTF8(data):
    """function that determines if a given data set
      represents a valid UTF-8 encoding"""

    def count(num):
        counter = 0
        for i in range(7, -1, -1):
            if (num >> i) & 1:
                counter += 1
            else:
                break
        return counter

    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            new = count(byte)
            if new == 0:
                continue
            if new == 1 or new > 4:
                return False
            num_bytes = new - 1
        else:
            if count(byte) != 1:
                return False
            num_bytes -= 1

    return num_bytes == 0
