#!/usr/bin/env python3
# Your classmates asked you to copy some paperwork for them. 
# You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need.

# Example:
# paperwork(5, 5) == 25
# Note: if n < 0 or m < 0 return 0!

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        total = n * m
        return total

print(paperwork(5,5))