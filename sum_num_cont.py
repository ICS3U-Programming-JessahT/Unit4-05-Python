#!/usr/bin/env python3

# Created By: Jessah
# Date: Nov 29, 2022
# This program ask the user for a number and it will
# After ask for more numbers to add up until it reaches
# The initial number


def main():
    # initialize sum and counter to 0
    sum = 0
    counter = 0

    # get the initial number from user
    initial_num_str = input("How many numbers do you want to add?: ")
    try:  # check if the input is valid
        initial_num_int = int(initial_num_str)
    except Exception:
        print("{} is an invalid input".format(initial_num_str))
    else:
        while counter < initial_num_int:  # while the counter is lower than initial num
            # get numbers to add from the user
            added_num_str = input(
                "What positive number do you want to add to the sum: "
            )
            try:  # check if the added number is valid
                added_num_int = int(added_num_str)
            except Exception:
                print("{} is invalid".format(added_num_str))
            else:
                if added_num_int > 0:
                    counter = (
                        counter + 1
                    )  # counter increases by 1 until it matches initial num
                    sum = sum + added_num_int  # added numbers increases the sum
                    print("{} was added to the sum".format(added_num_str))
                    if (
                        counter > initial_num_int
                    ):  # when the counter is greater continue
                        continue
                else:
                    print("{} is invalid".format(added_num_int))
        print("")
        # display the overall sum to user
        print("The overall sum is {}".format(sum))


if __name__ == "__main__":

    main()
