# lambda function
a = [(3, 4), (7, 1), (5, 9), (2, 2)]

# key sort mosavi ba lambda har x ke gerefti x[1] ro estefadeh kon
a.sort(key=lambda x: x[1])

print(a)


# map = ye list daram az koli chiz va ma function ru be done done haryek az ajzaye list apply kon
#
mylist = [1, 4, 5, 8, 7, 6]  # mikhaeim harkodom ro 2 barabar konim
# map(func , list) # map kon ye function be ye list
result = list(map(lambda x: x*2, mylist))
print(result)
numbers = [10, 11, 8, 7, 100, 6, 7, 21]
# onaei ke bozorgtar az 10 hastan ru big seda konimage kochik tar bood small

result2 = list(map(lambda x: "big" if x > 10 else "small", numbers))
print(result2)

# filter= ye list daram va filteresh kon ba funcitoni ke man daram

mylist2 = [1, 5, 6, 7, 8, 10, 11]
result3 = list(filter(lambda x: x % 2 == 0, mylist2))  # faghat zooj haro mide
print(result3)

# reduce
