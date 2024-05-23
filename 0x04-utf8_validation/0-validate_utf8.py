#!/usr/bin/python3
"""
This script includes the function validUTF8, which
checks if a provided data sequence is a valid UTF-8 encoding.
"""

def validUTF8(data):
    """
    Checks if a provided data sequence is a valid UTF-8 encoding.
    """
    n_bytes = 0

    for b in data:
        if n_bytes == 0:
            if b >> 3 == 0b11110:
                n_bytes = 3
            elif b >> 4 == 0b1110:
                n_bytes = 2
            elif b >> 5 == 0b110:
                n_bytes = 1
            elif b >> 7 == 0b1:
                return False
        else:
            if b >> 6 != 0b10:
                return False
            n_bytes -= 1

    return n_bytes == 0
