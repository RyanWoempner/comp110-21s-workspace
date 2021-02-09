"""An exercise in remainders and boolean logic."""

__author__ = "730362169"

carolina: int = int(input("Enter an int: "))

if carolina % 2 == 0 and carolina % 7 == 0:
    print(" TAR HEELS ")
else:
    if carolina % 7 == 0:
        print(" HEELS ")
    else:
        if carolina % 2 == 0:
            print(" TAR ")
        else:
            print(" CAROLINA ")