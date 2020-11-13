
letters = ['b', 'a', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100
combined = zeros + letters
numbers = list(range(20))  # create list from 0 to 20
chars = list('Hello world')
print(len(chars))
print(zeros)
print(combined)
print(numbers)
print(chars)
letters[0] = "A"
print(letters[0:3])
print(letters[:])  # copy of original list
print(letters[::2])  # 2 is step
numberss = list(range(20))
print(numberss[::2])  # // even numbers
print(numberss[::-1])  # //reverse order


numberss = [1, 2, 3, 4, 5, 6, 7]
# list unpacking and rest of calue in others
first, second, third, *other = numberss

first = numbers[0]
second = numbers[1]
third = numbers[2]

# unpacking


# loop
for letter in letters:
    print(letter)

# enumerate => show enumerate object in tuple as index of list

for letter in enumerate(letters):
    print(letter[0], letter[1])
    # or
for index, letter in enumerate(letters):  # using unpacking
    print(index, letter)

    # addin and remove item
letter.append("Z")
letter.insert(0, "-")  # 0 is index
# remove
letter.pop()  # empty is lastone or put index
letter.pop(0)
letter.remove("b")  # first occureness of b and dont know the inddex of item
del letters[0]  # range of items
del letters[0:3]
letters.clear()  # remoce all items in list
if "d" in letters:
    letter.index("a")  # hsow index of item

letters.count("d")

numbersss = [1, 2, 3, 65, 7, 4, 2, 5, 1]
print(numbersss.sort())
print(numbersss.sort(reverse=True))

sorted(numbersss)  # return new list -- it's
sorted(numbersss, reverse=True)


item = [
    ("Product1", 19),
    ("Product2", 9),
    ("Product3", 21),
    ("Product4", 5),
]


def sort_item(item):
    return item[1]


item.sort(key=sort_item)  # key is another function and just referese
# that was ugly

# new methods
# lambda function
item.sort(key=lambda item: item[0])

# map funciton
# transfer this list into another shape

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# get lambda and apply its on every item in iterable
x = list(map(lambda item: item[1], items))
print(x)

for item in x:
    pritn(item)

# filter
# get item with prices ...

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
