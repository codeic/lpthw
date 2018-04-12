# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Mistakes:
# 1. 
# Traceback (most recent call last):
#  File "ex13.py", line 5, in <module>
#    script, first, second, third = argv
# ValueError: need more than 1 value to unpack
    # I didn't payed attention to this part in the book:
    # "Run the program like this (and you must pass three command line arguments)"
    # Resolved. I typed:
    # python ex13.py joe sue magna
    
