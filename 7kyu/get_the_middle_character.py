#!/usr/bin/env python3

# You are going to be given a word. 
# Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

# #Input
# A word (string) of length 0 < str < 1000. 
# You do not need to test for this. 
# This is only here to tell you that you do not need to worry about your solution timing out.

# #Output
# The middle character(s) of the word represented as a string.


def get_middle(s):
    w_size = len(s)
    print("\n" + str(len(s)))
    mid_size = s[round(w_size//2) -1]

    # if even (PAIR)
    if len(s) %2 == 0:
        return(mid_size + s[round(w_size//2)])
    # if odd    (IMPAIR) 
    else:
        return s[round(w_size//2)]

print("Should get a, and get: " + get_middle("a"))      # a
print("Should get ab, and get: " + get_middle("ab"))     # ab
print("Should get b, and get: " + get_middle("abc"))    # b
print("Should get bc, and get: " + get_middle("abcd"))   # bc
print("Should get c, and get: " + get_middle("abcde"))  # c
print("Should get cd, and get: " + get_middle("abcdef")) # cd 
print("Should get d, and get: " + get_middle("abcdefg"))# d
print("Should get de, and get: " + get_middle("abcdefgh"))# de
print("Should get e, and get: " + get_middle("abcdefghi"))# e
print("Should get d, and get: " + get_middle("aLxeIxdyypcIM")) # d