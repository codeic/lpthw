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
def foo(x, y):
    print "First: %r!" % x
    print "Second %r!" % y
    print "Now both: %r %r!" % (x, y)

# 1)    
#foo("Batman", "Catwoman")

# 2)
#x = "Catwoman in red"
#y = "Batman in orange"
#foo(x, y)

# 3)
#funny_word_1 = raw_input("Please insert a funny word: ")
#funny_word_2 = raw_input("Please insert another funny word: ")
#foo(funny_word_1, funny_word_2)

# 4)
target = open(raw_input("Insert the filename: "), 'a')
target.write(str(foo("Bitcoin", "Litecoin")))

    
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
