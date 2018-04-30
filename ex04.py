# -*- coding: utf-8 -*-

# Interesting notes from Web (https://anh.cs.luc.edu/python/hands-
# on/3.1/handsonHtml/variables.html) about variable assignments:

# Try
# width = 10
# Nothing is displayed by the interpreter after this entry, so it is 
# not clear anything happened. Something has happened. This is an 
# assignment statement, with a variable, width, on the left. A variable 
# is a name for a value. An assignment statement associates a variable 
# name on the left of the equal sign with the value of an expression 
# calculated from the right of the equal sign. Enter
# width
# Once a variable is assigned a value, the variable can be used in 
# place of that value. The response to the expression width is the same 
# as if its value had been entered.

# The equal sign is an unfortunate choice of symbol for assignment, 
# since Python’s usage is not the mathematical usage of the equal sign. 
# If the symbol ↤ had appeared on keyboards in the early 1990’s, it 
# would probably have been used for assignment instead of =, 
# emphasizing the asymmetry of assignment. In mathematics an equation 
# is an assertion that both sides of the equal sign are already, in 
# fact, equal. A Python assignment statement forces the variable on the 
# left hand side to become associated with the value of the expression 
# on the right side. 




# This variable assigns number of cars.
cars = 100

# This variable assigns quantity of space in a car.
space_in_a_car = 4.0

# This variable assigns quantity of drivers.
drivers = 30.0

# This variable assings number of passengers.
passengers = 90

# This variable assigns difference between variables cars and drivers.
cars_not_driven = cars - drivers

# This variable assings value of variable drivers.
cars_driven = drivers

# This variable assigns product of variables cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car

# This variable assigns quotient of variables passengers and cars_driven.
average_passengers_per_car = passengers / cars_driven

# Zed had this problem:

# Traceback (most recent call last):
# File "ex4.py", line 8, in <module>
# average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined

# which lies in the fact that variable carpool_capacity is derived from variable cars_driven, which is equal to variable drivers. 
# Variable drivers is float point. That, for reason not known to me, is a problem. 
# Google is not much of a help.

# I will leave this text about float point, for sake of future laughs. Float point is NOT the problem. Problem is in typing car_pool_capacity instead of carpool_capacity.

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


# Study Drills:

# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
# A: Nothing. Result is still a float point. But if I change other variable too (drivers, which is equal to cars_driven), then it becomes an integer.

# 2. Remember that 4.0 is a “floating point” number. Find out what that means.
# A: Float point is number with decimals.

# 3. Write comments above each of the variable assignments.
# 4. Make sure you know what = is called (equals) and that it’s making names for things.
# 5. Remember that _ is an underscore character.
# 6. Try running Python as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
