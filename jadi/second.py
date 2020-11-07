
# # generator
# # function haye maoli tu mohasebat sangin memory va time ziad migirdad
# # ma generator darim ke mese function ha hast ke ma loghat jadid darim be name yield
# # ma tu fuction mamoli mohasebat anjam mishe bad javab return mishe


# # def firstn():
# #     return(1, 2, 3)


# # firstn()

# def firstn():
#     yield 1
#     yield 2
#     yield 3

# # harmoqe barnamaro ejra konim mirese be avalin yeild va meghdar barmigarde va midane kojaeye barname hast
# # dafe bad ke barname seda zade mishe midone koja hast va 2 ru barmigardonat
# # type in generator object hast
# # bishtar tu for ya whie ya iteraotr esetefadeh mishe


# # for i in firstn():
# #     print(i)

# #shabi for i in (1,2,3) ke yekzarb dar memory sakhte mishe va baes mishe memory por she


# writing the program to count 1 to n and return it
def firstn(n):
    number = 0
    while (number < n):
        yield number
        number += 1


for i in firstn(10):
    print(i)

# fagaht mitoshe in function ru tu ye initeratoraa seda bezanim
# javaba sari miad masalan felan karo kon natijaro yield kon va code ha ziba tareee
# beja zakhire melion ha addad ya jahaei ke nemidonaim cheghadr addad darim yani ye range darim
