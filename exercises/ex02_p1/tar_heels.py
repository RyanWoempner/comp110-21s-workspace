"""Tar Heels exercise redux as a structured program."""

__author__ = "YOUR 9-DIGIT PID"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    carolina: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(carolina))

# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(carolina: int) -> str:
    if carolina % 2 == 0 and carolina % 7 == 0:
        return (" TAR HEELS ")
    else:
        if carolina % 7 == 0:
            return (" HEELS ")
        else:
            if carolina % 2 == 0:
                return (" TAR ")
    return(" CAROLINA ")

if __name__ == "__main__":
    main()
