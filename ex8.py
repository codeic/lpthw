# -*- coding: utf-8 -*-

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing",
    "So, I said goodnight."
)
# Study Drills
# 1. Do your checks of your work, write down your mistakes, and try 
# not to make them on the next exercise.

    # A: Mistakes:
    # 1.1 Traceback (most recent call last):
    #  File "ex8.py", line 12, in <module>
    #    "So, I said goodnight."
    # TypeError: not enough arguments for format string

    # Resolved, line 10 missed comma sign.

    # 1.2 I forgot to type in line 8.
    
# 2. Notice that the last line of output uses both single-quotes 
# and double-quotes for individual pieces. Why do you think that is?
# A: I guess it is because string already has single-quote inside it.


