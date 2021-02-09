"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730362169"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...

print("Your fortune cookie says...")

fortune: int = (randint(1, 4))

if fortune == 1:
    print("Good things are coming your way.")
else:
    if fortune == 2:
        print("Money will come to you.")
    else:
        if fortune == 3:
            print("Better days are ahead.")
        else:
            print("You have a bright future")

print("Now, go spread positive vibes.")