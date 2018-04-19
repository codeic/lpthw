# -*- coding: utf-8 -*-

# This line imports executable statement argv from sys module.
from sys import argv

# This line adds arguments to argv.
script, filename = argv

# This variable assigns function open which consists of one argument,
# filename.
txt = open(filename)

# This line prints sentence.
print "Here's your file %r:" % filename

# This line prints result of call of a function on variable txt.
print txt.read()

# This line prints sentence.
print "Type the filename again:"

# This variable assigns function with string as argument.
file_again = raw_input("> ")

# This variable assigns function open with variable file_again as
# argument.
txt_again = open(file_again)

# This line prints result of call of a function on variable.
print txt_again.read()

# Study Drills
# This is a big jump, so be sure you do this Study Drill as best you 
# can before moving on.

# 1. Above each line, write out in English what that line does.

# 2. If you are not sure, ask someone for help or search online. Many 
# times searching for “python THING” will find answers for what that 
# THING does in Python. Try searching for “python open.”

# 3. I used the name “commands” here, but they are also called 
# “functions” and “methods.” Search around online to see what other 
# people do to define these. Do notworry if they confuse you. It’s 
# normal for programmers to confuse you with vast extensive knowledge.

# 4. Get rid of the part from lines 10–15 where you use raw_input and 
# try the script then.

# 5. Use only raw_input and try the script that way. Think of why one 
# way of getting the filename would be better than another.

# 6. Run pydoc file and scroll down until you see the read() command 
# (method/function). See all the other ones you can use? Skip the ones # that have __ (two underscores) in front because those are junk. Try 
# some of the other commands.

# 7. Start python again and use open from the prompt. Notice how you 
# can open files and run read on them right there?
    # A: This required more time than I expected. Final result was something
    # like this:
x = "ex15_sample.txt"
print open(x).read()

# 8. Have your script also do a close() on the txt and txt_again 
# variables. It’s important to close files when you are done with them.
    # A: At first, I wasn't sure how to do this. Should I put close 
    # like this, or append it to variable value... I saw this at 
    # http://tiny.cc/a0ptsy
    # and it seems it works, since I don't see any errors.
txt.close()
txt_again.close()
    # There is also this from Stack Overflow:
    # http://tiny.cc/szptsy 
    # from where I would highlight few things:
    # "When you leave the nested block, Python automatically calls 
    # f.close() for you"
    # and 
    # "Also if someone does explicitly close the file, will it have any 
    # undesirable effect?
    # In general, this is a bad thing to do.
    # However, file objects go out of their way to make it safe. It's 
    # an error to do anything to a closed file—except to close it again.
