# This line imports *variable* from a module.
# (https://stackoverflow.com/a/46810537/4455055)
from sys import argv

# This line gives two arguments to argv. First is this script itself,
# second is a input file, 'test.txt' in this case.
script, input_file = argv

# This line defines function with one parameter. The function is
# is inteded to print contents of the parameter after reading it.
def print_all(f):
# This line reads value given to parameter and prints it out.
    print f.read()

# This line defines function with one parameter, same as in previous
# function.
def rewind(f):
# This line seeks for reference point ('f') which is the beginning of the file, since '0' is given as 'from_what' parameter.
# (https://stackoverflow.com/a/11696554/4455055)
    f.seek(0)

# This line defines function with one new and one parameter from 
# previous functions.
def print_a_line(line_count, f):
# This line prints first parameter, then reads one line of second 
# parameter.
    print line_count, f.readline()

# This line assings value to variable - opening of a given paramater.
current_file = open(input_file)

# This line prints sentence.
print "First let's print the whole file:\n"
# This line calls function with variable as a given parameter.
print_all(current_file)

# This line prints sentence.
print "Now let's rewind, kind of like a tape."

# This line calls function with variable as a given parameter.
rewind(current_file)

# This line prints sentence.
print "Let's print three lines:"

# This line assigns value to variable.
current_line = 1
# This line calls function and gives it two variables as parameters.
print_a_line(current_line, current_file)

# This line assigns value to variable and increments it.
current_line = current_line + 1
# This line calls function and gives it two variables as parameters.
print_a_line(current_line, current_file)

# This line assigns value to variable and increments it.
current_line = current_line + 1
# This line calls function and gives it two variables as parameters.
print_a_line(current_line, current_file)

# Study Drills

# 1. Go through and write English comments for each line to understand 
# what's going on.

# 2. Each time print_a_line is run you are passing in a variable 
# current_line. Write out what current_line is equal to on each 
# function call, and trace how it becomes line_count in print_a_line.

# 3. Find each place a function is used, and go check its def to make 
# sure that you are giving it the right arguments.

# 4. Research online what the seek function for file does. Try pydoc 
# file and see if you can figure it out from there.

# 5. Research the shorthand notation += and rewrite the script to use 
# that.
