#!/usr/bin/env python3

# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.


def find_short(s):
    # Split the single string into a multiple one
    words = s.split(" ")

    # define the first value as the shortest word
    shortest_word = len(words[0])

    # for each word of the list, if it is shorter update shortest_word
    for word in words:
        if len(word) < shortest_word:
            shortest_word = len(word)
   
    return shortest_word
   
print(find_short("bitcoin take over the world maybe who knows perhaps"))
