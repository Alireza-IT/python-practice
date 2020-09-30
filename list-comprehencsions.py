items = [
    ("productions", 10),
    ("productions", 6),
    ("productions", 13),
    ("productions", 2),
]
prices = list(map(lambda item: item[1], items))  # return new list

# filltering base on conditions
filtered = list(filter(lambda item: item[1] >= 10, items))

# comprehension
# [expression for item in items] #apply expression on each item in loop
prices = [item[1] for item in items]  # recommended
# [] define new list and first item is item that comes out
filterd = [item for item in items if item[1] >= 10]

# zip function
# combined list into tuple list
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# because we have 2 diff list

print(list(zip(list1, list2)))
