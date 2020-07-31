"""
Bit manipulation is not necessarily easy to visualize.

This module helps with that.

For use with:
https://tutorialedge.net/compsci/bit-manipulation-for-beginners/
"""


def printret(x, y):
    "Print and return"
    print(x)
    return y


def bit(num, pad=8):
    "Print and return a bits with a specified padding"
    return printret(
        bin(num).strip("'")[2:].rjust(pad),
        num
    )


if __name__ == '__main__':
    print(
        bit(bit(4) | bit(3))
    )
