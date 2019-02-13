#!/usr/bin/env python
"""
Given a string of parentheses, 
write a function to compute the minimum number of parentheses 
to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", 
you should return 1. 
Given the string ")(", 
you should return 2, 
since we must remove all of them.
"""

from math import sqrt, log, e
from random import choice, random
import sys

__author__ = "Abhishek Srivastava"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Abhishek Srivastava"
__email__ = "abhs26@gmail.com"
__status__ = "Production"

def min_num_paran(s_name):
    count = 0
    count_1 = 0
    for c_charval in s_name:
        if c_charval is "{":
            count += 1
        elif c_charval is "}":
            if count > 0:
                count -= 1
            else:
                count_1 += 1
    print(count + count_1)
    
if __name__ == '__main__':    #code to execute if called from command-line
    if len(sys.argv) > 0:
        min_num_paran(sys.argv[1])