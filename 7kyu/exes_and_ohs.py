#!/usr/bin/env python3

# Check to see if a string has the same amount of 'x's and 'o's. 
# The method must return a boolean and be case insensitive. 
# The string can contain any char.

# Examples input/output:
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    count_x = 0
    count_o = 0

    for char in s:
        if char == 'x' or char == 'X':
            count_x += 1
        elif char == 'o' or char == 'O':
            count_o += 1


    print(count_o)
    print(count_x)
    if count_o == count_x:
        return True
    else:
        return False



