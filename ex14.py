# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
prompt = 'TYPE YOUR ANSWER AS FAST AS YOU CAN -->> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# Study Drills
# 1. Find out what Zork and Adventure were. Try to find a copy and 
# play it.

# 2. Change the prompt variable to something else entirely.

# 3. Add another argument and use it in your script.
    # A:
print "Now, most importantly: Did you ever read 'Hitchhiker's Guide'?"
book = raw_input(prompt)
print "So your answer is %r, but since I still don't know anything about answers, please stay here until I learn some more." % book

# 4. Make sure you understand how I combined a """ style multiline 
# string with the % format activator as the last print.
