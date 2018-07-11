# -*- coding: utf-8 -*-

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first on and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# 5 >>> import ex25
# 6 >>> sentence = "All good things come to those who wait."
# 7 >>> words = ex25.break_words(sentence)
# 8 >>> words
# 9 ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
# 10 >>> sorted_words = ex25.sort_words(words)
# 11 >>> sorted_words
# 12 ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# 13 >>> ex25.print_first_word(words)
# 14 All
# 15 >>> ex25.print_last_word(words)
# 16 wait.
# 17 >>> wrods
# 18 Traceback (most recent call last):
# 19 File "<stdin>", line 1, in <module>
# 20 NameError: name 'wrods' is not defined
# 21 >>> words
# 22 ['good', 'things', 'come', 'to', 'those', 'who']
# 23 >>> ex25.print_first_word(sorted_words)
# 24 All
# 25 >>> ex25.print_last_word(sorted_words)
# 26 who

# 27 >>> sorted_words
# 28 ['come', 'good', 'things', 'those', 'to', 'wait.']
# 29 >>> sorted_words = ex25.sort_sentence(sentence)
# 30 >>> sorted_words
# 31 ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# 32 >>> ex25.print_first_and_last(sentence)
# 33 All
# 34 wait.
# 35 >>> ex25.print_first_and_last_sorted(sentence)
# 36 All
# 37 who

# Study Drills

# 1. Take the remaining lines of the WYSS output and figure out what they are 
# doing. Make sure you understand how you are running your functions in the 
# ex25 module.
    # A:
    # I was wandering why there are no first and last words after on the line
    # 22, and I found this explanations about pop():
    # "Remove the item at the given position in the list, and return it. 
    # If no index is specified, a.pop() removes and returns the last item 
    # in the list."
    # https://docs.python.org/2/tutorial/datastructures.html

# 2. Try doing this: help(ex25) and also help(ex25.break_words). 
# Notice how you get help for your module and how the help is those odd """ 
# strings you put after each function in ex25? Those special strings are called 
# documentation comments and we’ll be seeing more of them.

# 3. Typing ex25. is annoying. A shortcut is to do your import like this: 
# from ex25 import *, which is like saying, “Import everything from ex25.” 
# Programmers like saying things backward. Start a new session and see how all 
# your functions are right there.

# 4. Try breaking your file and see what it looks like in Python when you 
# use it. You will have to quit Python with CTRL- D (CTRL- Z on Windows) to be 
# able to reload it.
