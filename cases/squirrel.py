#!/usr/bin/env python3

def squirrel(N):
    """Function return first number of factorial(N)"""

    def factorial(num):
        """Recursive calculate factorial N"""
        if type(num) == int and num >= 0:
            result = lambda num: result(num - 1) * num if num > 0 else 1
            return result(num)
        else:
            raise TypeError(
                "The given value must be positive integer, not %s" % (
                    type(num) if type(num) != int
                    else "negative"))
    return int(str(factorial(N))[0])

