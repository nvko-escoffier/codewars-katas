#!/usr/bin/env python3
# In this simple assignment you are given a number
#  and have to make it negative. But maybe the number is already negative?


def make_negative( number ):
    if number > 0:
        return number-number*2
    elif number <0:
        return number
    else:
        return 0


print(make_negative(42))
