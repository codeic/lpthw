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
    # "Run the program like this (and you must pass three command line 
    # arguments)"
    # Resolved. I typed:
    # python ex13.py joe sue magna
    
# Study Drills
# 1. Try giving fewer than three arguments to your script. See that 
# error you get? See if you can explain it.
    # A: I've got this, after running 'python ex13.py foo bar':
        # Traceback (most recent call last):
        #   File "ex13.py", line 5, in <module>
        #   script, first, second, third = argv
        # ValueError: need more than 3 values to unpack
    # It wants more than 3 (script is the first, and foo bar are the
    # latter two. If I type in more than 4 values, it will print:
        # Traceback (most recent call last):
        #   File "ex13.py", line 5, in <module>
        #   script, first, second, third = argv
        # ValueError: too many values to unpack

# 2. Write a script that has fewer arguments and one that has more. 
# Make sure you give the unpacked variables good names.

# 3. Combine raw_input with argv to make a script that gets more input 
# from a user.
    # A:
foo = raw_input("Did you overthinked this? ")
print "%s, I think..." % foo

# 4. Remember that modules give you features. Modules. Modules. 
# Remember this because we’ll need it later.
