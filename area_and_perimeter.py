#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on April 2021
# This program calculates the perimeter and area of a 15 mm radius circle

import math


def main():
    # this function calculates perimeter and area

    print("If a circle has the following radius:")
    print("15 mm")
    print("")
    print("The area is {} mm².".format(math.pi * 15 ** 2))
    print("The perimeter is {} mm.".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
