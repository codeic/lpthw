# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists
from os import rename

script, from_file, to_file = argv

# print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()
    # A:
indata = open(from_file).read()

# print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

# print "Alright, all done."

out_file.close()

# Commented out, because there was no need for it anymore.
# in_file.close()

# Study Drills
# 1. Go read up on Python’s import statement, and start python to try 
# it out. Try importing some things and see if you can get it right. 
# It’s alright if you do not.
    # A: My first attempt was
    # import os
    # and command was
    # os.rename(src, dst)
    # and then I tried to find out the difference between these two ways
    # of importing and stumbled upon this:
    # https://stackoverflow.com/questions/710551/
    # then tried to import it like this.
    # Main difference I can find (and important to me, at this moment)
    # is that whit this way you don't need to type
    # os.rename
rename("test.txt", "test1.txt")
    # I also tried with one built-in 
print "Hash value of input file is: %d" % hash(indata)

# 2. This script is really annoying. There’s no need to ask you before 
# doing the copy, and it prints too much out to the screen. Try to make 
# it more friendly to use by removing features.

# 3. See how short you can make the script. I could make this one line 
# long.
    # A: My attempt is written in ex17v2.py.

# 4. Notice at the end of the WYSS I used something called cat? It’s an 
# old command that “concatenates” fi les together, but mostly it’s just 
# an easy way to print a file to the screen. Type man cat to read 
# about it.

# 5. Windows people, find the alternative to cat that Linux/OSX people 
# have. Do not worry about man since there is nothing like that.

# 6. Find out why you had to do output.close() in the code.
    # A: First, I found this: 
    # https://stackoverflow.com/questions/8995523/
    # And then, by googling "leak file descriptors", found this blog:
    # https://martin-ueding.de/articles/c-file-descriptors/index.html
    # Which I ran and got the same result. Then I realized that I 
    # don't know what 'file descriptors' are. Wikipedia says:
    # "In Unix and related computer operating systems, a file 
    # descriptor (FD, less frequently fildes) is an abstract indicator 
    # (handle) used to access a file or other input/output resource, 
    # such as a pipe or network socket."
    # https://www.wikiwand.com/en/File_descriptor
