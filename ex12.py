# -*- coding: utf-8 -*-

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
# Study Drills
# 1. In Terminal, where you normally run python to run your scripts, 
# type pydoc raw_input.
# Read what it says. If you’re on Windows try python - m pydoc 
# raw_input instead.
# A: It says: "(...) Read a string from standard input. (...)"
# 2. Get out of pydoc by typing q to quit.
# 3. Look online for what the pydoc command does.
# 4. Use pydoc to also read about open, file, os, and sys. 
# It’s alright if you do not understand those; just read through and 
# take notes about interesting things.
