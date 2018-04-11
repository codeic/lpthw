# -*- coding: utf-8 -*-

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#Study Drills
# 1. Go online and find out what Python’s raw_input does.
# A: From python.org 
# (https://docs.python.org/2/library/functions.html#raw_input)
# "If the prompt argument is present, it is written to standard output
# without a trailing newline. The function then reads a line from input,
# converts it to a string (stripping a trailing newline), and returns
# that. When EOF is read, EOFError is raised."
# From stackoverflow.com
# (https://stackoverflow.com/a/5563119/4455055)
# "It presents a prompt to the user (the optional arg of raw_input
# ([arg])), gets input from the user and returns the data input by the 
# user in a string."

# 2. Can you find other ways to use it? 
# Try some of the samples you find.
# A: I can't seem to find others methods of usage. There are 
# combinations, but basic form remains the same:
print "Enter first number: ",
foo = raw_input()
print "Enter second number: ",
bar = raw_input()
print int(foo)+int(bar)

# 3. Write another “form” like this to ask some other questions.
# A: 
print "Why am I learning Python?",
answer = raw_input()
print (answer)
print "Are you sure?"

# Mistakes:
    # 1. 
    # I wrote function raw_input wrong, without ().

# 4. Related to escape sequences, try to find
# out why the last line has '6\'2"' with that \' sequence. 
# See how the single-quote needs to be escaped 
# because otherwise it would end the string?
# A: Because %r enclose string with single-quotes?

