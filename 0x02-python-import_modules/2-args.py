#!/usr/bin/python3
import sys


def main():

    argv = sys.argv[1:]
    num_args = len(argv)

    print("Number of argument(s):", end=" ")
    if num_args == 0:
        print(".", end="\n\n")
    elif num_args == 1:
        print("1 argument:", end="\n")
    else:
        print("{} arguments:".format(num_args), end="\n")

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
        if __name__ == "__main__":
            main()
