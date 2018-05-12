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
first_q = "\033[91m" + "I've heard there are many 'coins', not only \
Bitcoin. Can you explain me what %s%s is?" + "\033[0m"
second_q = "\033[91m" + "What's the usage of %r?" + "\033[0m"
third_q = "\033[91m" + "%s is more than $%d worth \
now over at exchanges.\n" + "\033[0m"

def foo(x, y, z):
    print first_q % (x, y)
    print second_q % (x + y)
    print third_q % (x + y, z)


# 1) With arguments
foo("Dark", "coin", 11)

# 2) With variables passed as arguments
x = "Lite"
y = "coin"
z = 22
foo(x, y, z)

# 3) With user input
random_word = raw_input("Type some random word: ")
foo(random_word, y, 33)
print "\033[91m" +  "P.S. Try searching the result over at cryptomarketcap.com, \
that coin may really exist\n" + "\033[0m"

# 4) Inside another function
def bar():
    foo(random_word, y, 44)
bar()

# 5) Using math
foo(x, y, z + 1000)

# 6) Assigning function to a variable
crypto = foo("Bit", y + " Cash", z + 850)

