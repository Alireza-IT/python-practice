from sys import getsizeof
values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)
print(getsizeof(values))
# make generator obj because above is not effiecient when we have lots of data and data set

values2 = (x * 2 for x in range(10))
# it's generaator adn has no len functions
# size of obj?? remain constant
print(getsizeof(values2))
