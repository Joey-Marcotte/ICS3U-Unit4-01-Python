#!/usr/bin/env python3

# Created by: Joey Marcotte
# Created on: October 2019
# This program shows adding up to a number


def main():
    # input
    added_number = 0
    total_number = 0
    number = input("Input the number: ")

    try:
        number_as_number = int(number)
        while number_as_number > added_number:
            # process
            print("+{0}".format(added_number))
            added_number = added_number + 1
            total_number = added_number + total_number

        print("+{0}".format(number_as_number))
        print("The answer is {0}".format(total_number))

    except(ValueError):
        print("That is not a valid number")


if __name__ == "__main__":
    main()
