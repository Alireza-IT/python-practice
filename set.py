# collection with no duplicate and not in order and does not have indexing
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first)

print(first | second)  # give us union jtema
print(first & second)  # give us intersect eshterak
print(first - second)
print(first ^ second)  # symetric diff

if 1 in first:
    print("yes")
