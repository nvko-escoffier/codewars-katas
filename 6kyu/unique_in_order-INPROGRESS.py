#!/usr/bin/env python3

#Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value 
# next to each other and preserving the original order of elements.

#EXAMPLE
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    string = list(iterable)
    print(len(string))
    # for index, obj in enumerate(iterable):
    #     if obj[index] == 0:
    #         print(obj)
    #     else:
    #         if obj != obj[index - 1]:
    #             print(obj)
  
    return string

## return A,B,C,D
#    unique_string = []
#    string = list(iterable)
#    print(string)
#    return sorted(set(iterable), key=iterable.index)

print(unique_in_order('AAAABBBCCDAAABBBBB'))
