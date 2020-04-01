#!/usr/bin/env python3
#
# done: March, 31th 2020
#
# Given 3 integers a ,b ,c, return the largest number obtained 
# after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , 
# and return the Maximum Obtained

#EXAMPLE
# With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:
# 1 * (2 + 3) = 5
# 1 * 2 * 3 = 6
# 1 + 2 * 3 = 7
# (1 + 2) * 3 = 9
# So the maximum value that you can obtain is 9.

#NOTE
# The numbers are always positive.
# The numbers are in the range (1  ≤  a, b, c  ≤  10).
# You can use the same operation more than once.
# It's not necessary to place all the signs and brackets.
# Repetition in numbers may occur .
# You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8

def expression_matter(a, b, c):
    num = [a,b,c]

    # Possibilities with the highest possible calculation
    # a+b+c
    # a*b*c
    # (a+b)*c
    # a*(b+c)
    # (a+c)*b

    calc1 = num[0] + num[1] + num[2]
    calc2 = num[0] * num[1] * num[2]
    calc3 = (num[0] + num[1]) * num[2]
    calc4 = num[0] * (num[1] + num[2])
    calc5 = (num[0] + num[1]) * num[2]
    find_highest = max([calc1, calc2, calc3, calc4, calc5])

    return find_highest 

print(expression_matter(1,2,3))