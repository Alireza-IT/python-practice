from pprint import pprint  # more control tp print staff  and much prettier

# find most repeatative character

sentence = "this is a common interview question"

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)
pprint(char_frequency, width=1)

# for sorting becuase dict is unsorted we can not sort ..we can sort only list so convert each pait to tuple and store in list
# items() is return all key value pairs as tuples
# sorted function get iterable and return list but not sort because dont know how to sort base on ewhat unless based on lambda
# freq of each character and 3argument for reversing
# lambda is anymous function that takes keyvalue paires and return value (1)
char_frequesncy_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)

print(char_frequesncy_sorted)
