import math
# comment
# \'
# \"
# \\
# \n
# \t

student_count = 1000
rating = 4.99
is_published = False
course_name = "python \n programming"
print(student_count)
message = """
Hi there is a text
"""
print(len(course_name))
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:])
first = 'alireza'
last = 'ashtari'
# full = first + " " + last
full = f"{first} {last}"
print(full)
print(course_name.lower())
print(course_name.title())
print(course_name.find("Pro"))  # show the index return the index
print(course_name.replace("p", "j"))
print(course_name.strip())  # remove whitespaces
print("pro" in course_name)  # return the booelan of existenxe
print("swift" not in course_name)

################################

x = 1 + 2j  # complex number
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 ** 3)
print(10 % 3)
print(10 / 3)  # return float
print(10 // 3)  # return int

x = 10
x = x + 3
x += 3

print(round(2.9))
print(abs(-2.9))
print(abs(-2.9))

print(math.ceil(2.2))  # math is object

x = input('please enter your number:')
print(type(x))
y = int(x) + 1
print(f" x:{x} , y:{y}")
# int(x)
# flout(x)
# str(x)
