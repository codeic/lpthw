# -*- coding: utf-8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat. And I like to \acuddle!"
joe = "Grey one, evil one."
sue = "Happy one, ain't I?!"
black_cat = "black"
white_cat = "white"

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Mistakes: 
    # 1. 
    # Traceback (most recent call last):
    #  File "ex10.py", line 14, in <module>
    #    print backslash_cat
    # NameError: name 'backslash_cat' is not defined
        # Resolved. Typo.
        
# while True:
#    for i in ["/", "-", "|", "\\", "|"]:
#        print "%s\r" % i,
        
    # 2.
    #   File "ex10.py", line 25
    # while True
    #        ^
    # SyntaxError: invalid syntax
        # Resolved. Missed ":" after True.
        
# Study Drills
# 1. Memorize all the escape sequences by putting them on flash cards.

# 2. Use ''' (triple- single- quote) instead. Can you see why you 
# might use that instead of """?
# A: Maybe when I want to use double-quotes inside the string?

# 3. Combine escape sequences and format strings to create a more
# complex format.
# A:
print "You wanna know \twho am I? \v%r\f" % joe
print "The other one? \t%s" % sue

# 4. Remember the %r format? Combine %r with double-quote and 
# single-quote escapes and print them out. Compare %r with %s.
# A:
print "Look at the \'%s one next to the \"%s!" % (black_cat, white_cat)
print "There is a \'%r one next to the \"%r!" % (black_cat, white_cat)

# Notice how %r prints it the way you’d write it in
# your file, but %s prints it the way you’d like to see it?
