#!/usr/bin/env python
"""
A rule looks like this:
A NE B
This means this means point A is located northeast of point B.
A SW C
means that point A is southwest of C.
Given a list of rules, check if the sum of the rules validate. For example:
A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.
A NW B
A N B
is considered valid.
"""

from math import sqrt, log, e
from random import choice, random


__author__ = "Abhishek Srivastava"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Abhishek Srivastava"
__email__ = "abhs26@gmail.com"
__status__ = "Production"

print("h")