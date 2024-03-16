#!/bin/bash/python3
import sys


def main():
    # Retrieve command-line arguments excluding the script name
    args = sys.argv[1:]
    # Convert arguments to integers and sum them up
    total = sum(int(arg) for arg in args)
    # Print the total sum
    print(total)

# Execute the main function only if the script is run directly (not imported)


if __name__ == "__main__":
    main()
