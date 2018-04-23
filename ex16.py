# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write("%r\n%r\n%r\n" % (line1, line2, line3)

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()

# Study Drills

# 1. If you feel you do not understand this, go back through and use 
# the comment trick to get it squared away in your mind. One simple 
# English comment above each line will help you understand or at least 
# let you know what you need to research more.

# 2. Write a script similar to the last exercise that uses read and 
# argv to read the file you just created.
    # A:
print """
If you want to read your file, please run script 'ex16v2.py' by typing\n
'python ex16v2.py test.txt'\n
Or you can do 'more test.txt' or 'less test.txt' or 'cat test.txt' but
that's not the point anyway....
"""

# 3. There’s too much repetition in this file. Use strings, formats, 
# and escapes to print out line1, line2, and line3 with just one 
# target.write() command instead of six.
    # A: Contemplating this took me more than an hour. I tried:
    # target.write(line1 + "\n" + line2 + "\n" + line3)
    # but that is without formats. Then I tried:
    # print "I'm going to write these to the file.%r" % target.write    
    # (line1 + "\n" + line2 + "\n" + line3)
    # which is overcomplicated and produces 'None' after running the 
    # script (but it does write to the file). Neither output 'None',
    # how the script worked or when (and why) should I use formats
    # is understandable to me.
    # So I gave up, googled some, and found great answer at SO
    # (https://stackoverflow.com/a/8691360/4455055).
    
# 4. Find out why we had to pass a 'w' as an extra parameter to open. 
# Hint: open tries to be safe by making you explicitly say you want to 
# write a file.
    # A: If we didn't specified 'w' mode, then it fould fall back to
    # default reading mode ('a'). From documentation on file class:
    # "The mode can be 'r', 'w' or 'a' for reading (default), writing 
    # or appending."

# 5. If you open the file with 'w' mode, then do you really need the 
# target.truncate()? Go read the docs for Python’s open function and 
# see if that’s true.
    # A: Reading documentation I came to this conclusion: Python opens
    # the file with 'w' mode, then it leaves it open, which is why
    # I got "invalid syntax" errors when tried removing truncate.
    # Since 'w' mode does truncate the file, but leaves it open,
    # I need to use 'truncate' method to keep file open.
