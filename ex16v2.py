# *-* coding: utf-8 *-*

from sys import argv

script, filename = argv

target = open(filename).read()
print target

# Mistakes:
    # 1.
    # I tried to type 
    # target.close()
    # but got this error:
        # Traceback (most recent call last):
        # File "ex16v2.py", line 12, in <module>
        # target.close()
        # AttributeError: 'str' object has no attribute 'close'
    # and found this answer on Stack Overflow:
        # (https://stackoverflow.com/a/12118621/4455055
        # "[File you are trying to close] is a string variable, which
        # contains contents of the file -- it has no relation to the 
        # file. The file descriptor you open with open([file]) will be 
        # close automatially: file sessions are closed after the 
        # file-objects exit the scope 
        # (in this case, immediately after '.read()')"
    # I tested that, succesfully:
x = open(filename)
x.close()

