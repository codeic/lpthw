# - - coding: utf- 8 - -

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)

# Study Drills
# 1. Change all the variables so there isn’t the my_ in front. Make sure you change the name
# everywhere, not just where you used = to set them.

# 2. Try more format characters. %r is a very useful one. It’s like saying “print this no matter
# what.”
# A:
print "Who are you really, Mr. %r?" % teeth

# 3. Search online for all the Python format characters.
# A: Here is a list: https://docs.python.org/2.4/lib/typesseq-strings.html

# 4. Try to write some variables that convert the inches and pounds to centimeters and kilos.
# Do not just type in the measurements. Work out the math in Python.
# A:
x = 55
y = 50
i = 2.5
p = 0.453592

print "I prefer TV with %d cm in diagonal." % (x * i)
print "I guess it won't be heavier than %d pounds." % (y * p)
# Notes: First time I typed it without brackets, and it gave me this error:
#    Traceback (most recent call last):
#      File "ex5.py", line 42, in <module>
#        print "I prefer TV with %d cm in diagonal." % x * i
#    TypeError: can't multiply sequence by non-int of type 'float'
# I googled it, but couldn't seem to find it. So I revised code from the book and tried adding brackets. 
# Still, I don't know why is it working.

