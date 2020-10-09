numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)  # print like this =>use * to print individual item like ... in js
print(*numbers)

values = list(range(5))
# or
# unpack any iteralabe like range means take individual values
values2 = [*range(5)]
print(*"hello")

# using  in combining the list
first = [1, 2]
second = [3]
values3 = [*first, *second]
print(values3)

# ud=sing in the dict
first1 = {"x": 1}
second2 = {"x": 10,  "y": 2}
combined = {**first1, **second2}
print(combined)
