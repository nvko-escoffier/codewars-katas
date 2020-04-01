#!/usr/bin/env python3


# Instructions (https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python)
# Your task is to make a function that can take any non-negative integer as a argument 
# and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.


def descending_order(num):
  list = []
  # Populate the list with all the character present into (num)
  for number in str(num):
      list.append(number)
  
  # Sort the list, then reverse it
  sorted_list = sorted(list, reverse=True)
  
  # Group characters of each array, 
  # then integrate it through "map" as .join takes only 1 arg
  sorted_list = ''.join(map(str, sorted_list))
  
  return int(sorted_list)


# This function is here for testing purpose
print(descending_order('126345234'))




