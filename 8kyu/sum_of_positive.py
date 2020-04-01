#!/usr/bin/env python3

# You get an array of numbers, return the sum of all of the positives ones.
# Example [1,-4,7,12] => 1 + 7 + 12 = 20
# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arr):
    print(arr)
    total=0
    
    # If array is empty -> return 0
    if len(arr) == 0:
        return 0
    
    # For each positives number, proceed to sum into total
    for item in arr:
        if item > 0:
            total=item+total
    return total

print(positive_sum([-1,2,3,-5]))


