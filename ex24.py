print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t \
    tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print "--------------------"
print poem
print "--------------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# This part was confusing a bit, but SO clarified it significantly:
# https://stackoverflow.com/a/30165240/4455055
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % \
    secret_formula(start_point)

# Study Drills

# 1. Make sure to do your checks: read it backward, read it out loud, and put
# comments above confusing parts.

# 2. Break the file on purpose, then run it to see what kinds of errors you get.
# Make sure you can fix it.
    # Here's a break and a fix!
try:
    start_point = "novel"
    print secret_formula(start_point)
except TypeError:
    print "You have entered %r as a value for start point, while it must be a \
number and not a string." % start_point
    start_point = int(raw_input("Please enter a number: "))
    print secret_formula(start_point)
