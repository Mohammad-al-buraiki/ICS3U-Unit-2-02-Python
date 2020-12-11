#!/usr/bin/env python3

# Created by: Mohammad-al-buraiki
# Created on December 2020
# This program calculates the area and perimeter of a rectangle

import math


def main():
    # this function calculates the area and the perimeter of a rectangle
    
    # input
    length = input("Enter the length of a rectangle (mm):")
    width = input("Enter the wedth of a rectangle (mm):")

    # process
    area = ((length)*(width))
    perimeter = (2*((length)+(width)))
    
    # output
    print("The area of a rectangle is {} mm²."
          .format(area))
    print("The perimeter of a rectangle is {} mm"
          .format(perimeter))


    if __name__ == "__main__":
        main()
