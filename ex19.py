# -*- coding: utf-8 -*-

# This line defines a new function with two parameters.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # This line prints a sentence and variable.
    print "You have %d cheeses!" % cheese_count
    # This line prints a sentence and variable.
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # This line prints a sentence.
    print "Man that's enough for a party!"
    # This line, also, prints a sentence.
    print "Get a blanket.\n"
    

# This line prints a sentence.
print "We can just give the function numbers directly:"
# This line assigns two parameters to a function.
cheese_and_crackers(20, 30)

# This line prints a sentence.
print "OR, we can use variables from our script:"
# This line assigns value to a variable.
amount_of_cheese = 19
# This does the same job.
amount_of_crackers = 50


# This line assigns previous two variables as parameters to a function.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# This line prints a sentence.
print "We can even do math inside too:"
# This line assigns parameters to a function and does some math.
cheese_and_crackers(10 + 20, 5 + 6)


# This line prints a sentence.
print "And we can combine the two, variables and math:"
# This line assigns parameters to a function and does math, again.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Study Drills

# 1. Go back through the script and type a comment above each line, 
# explaining in English what it does.

# 2. Start at the bottom and read each line backward, saying all the 
# important characters.

# 3. Write at least one more function of your own design, and run it 
# 10 different ways.
    # A:
    
# For this drill, I found massive help over at this blog:
# https://www.josharcher.uk/code/lpthw-exercise-19-functions-variables/


# These three lines consists out of three variables. Each assigns
# value in a form of collored sentence.
first_q = "\033[91m" + "Can you explain me what %s%s is?" + "\033[0m"
second_q = "\033[91m" + "What's the usage of %r?" + "\033[0m"
third_q = "\033[91m" + "%s is more than $%d worth\
now over at exchanges."  + "\033[0m"

def foo(x, y):
    print  first_q % (x, y)\


# 1) With arguments
foo("Bit", "coin")

# 2) With variables passed as arguments
x = "Lite"
y = "coin"
foo(x, y)

# 3) With user input
random_word = raw_input("Type some random word: ")
foo(random_word, y)
print "P.S. Try searching the result over at cryptomarketcap.com, \
that coin may really exist."

# 4) Combined with another function
def bar():
    print third_q % (foo, 11)

bar()
    
    
# [] 1. Did you start your function definition with def?

# [] 2. Does your function name have only characters and _ 
# (underscore) characters?

# [] 3. Did you put an open parenthesis (right after the function name?

# [] 4. Did you put your arguments after the parenthesis (separated by 
# commas?

# [] 5. Did you make each argument unique (meaning no duplicated 
# names)?

# [] 6. Did you put a close parenthesis and a colon ): after the 
# arguments?

# [] 7. Did you indent all lines of code you want in the function four 
# spaces? No more, no less.

# [] 8. Did you “end” your function by going back to writing with no 
# indent (dedenting we call it)?


# And when you run (“use” or “call”) a function, check these things:

# [] 1. Did you call/use/run this function by typing its name?

# [] 2. Did you put the ( character after the name to run it?

# [] 3. Did you put the values you want into the parenthesis separated 
# by commas?

# [] 4. Did you end the function call with a ) character?)
