#!/usr/bin/env python
"""
Given three 32-bit integers x, y, and b,
return x if b is 1 and y if b is 0, 
using only mathematical or bit operations. 
You can assume b can only be 1 or 0.
"""
import sys

__author__ = "Abhishek Srivastava"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Abhishek Srivastava"
__email__ = "abhs26@gmail.com"
__status__ = "Production"

def check_bit(x, y, b):
    mask = 0
    return (( int(b) ^ mask ) and x ) or (( int(b) ^ (~mask) ) and y )


if __name__ == "__main__":
    if len(sys.argv) > 3:
        print(check_bit(sys.argv[1], sys.argv[2], sys.argv[3]))
