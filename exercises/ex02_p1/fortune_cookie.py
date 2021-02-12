"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730362169"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")

fortune: int = (randint(1, 4))

def fortune_cookie() -> str:
    if fortune == 1:
        return ("Good things are coming your way.")
    else:
        if fortune == 2:
            return ("Money will come to you.")
        else:
            if fortune == 3:
                return ("Better days are ahead.")
    return ("You have a bright future.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
