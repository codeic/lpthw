tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Mistakes: 
    # 1. 
    # Traceback (most recent call last):
    #  File "ex10.py", line 14, in <module>
    #    print backslash_cat
    # NameError: name 'backslash_cat' is not defined
        # Resolved. Typo.
