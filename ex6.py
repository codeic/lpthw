# - - coding: utf- 8 - -

# This variable assigns number of people.
x = "There are %d types of people." % 10

# This variable assigns word.
binary = "binary"

# This variable assigns word.
do_not = "don't"

# This variable assigns sentence with two previous variables.
# Here is first place where string is put into string.
y = "Those who know %s and those who %s." % (binary, do_not)

# This prints variable x.
print x

# This prints variable y.
# Here is second place where string is put into string.
print y

# This prints sentence.
# Here is third place where string is put into string.
print "I said: %r." % x

# This prints sentence.
# Here is fourth place where string is put into string.
print "I also said: '%s'." % y

# This variable assings boolean value.
hilarious = False

# This variable assigns sentence.
joke_evaluation = "Isn't that joke so funny?! %r"

# This prints two previous variables. I don't understand why is it % sign in the middle.
print joke_evaluation % hilarious

# This variable assings sentence.
w = "This is the left side of..."

# This variable assings sentence.
e = "a string with a right side."

# This prints two previous variables.
print w + e

# Study Drills
# 1. Go through this program and write a comment above each line explaining it.
# 2. Find all the places where a string is put inside a string. There are four places.
# 3. Are you sure there are only four places? How do you know? Maybe I like lying.

# 4. Explain why adding the two strings w and e with + makes a longer string.
# A: I don't see any other answer than 'Python does it that way'.
# But I found this:
# "The plus operation with strings means concatenate the strings. Python looks at the type of operands before deciding what operation is associated with the +."
# from "https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/strings1.html#string-concatenation". 
# I also found out that you can do this:
print "Hello"*2+"world"*2
