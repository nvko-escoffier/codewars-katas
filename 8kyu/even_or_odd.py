#!/usr/bin/env python3

# Create a function (or write a script in Shell) that takes 
# an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if (number % 2) != 0:
        return 'Odd'
    else:
        return 'Even'

print(even_or_odd(37489364893643))