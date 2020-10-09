from timeit import timeit  # calculate the execution time of program

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less")
    return 10 / age
#rasie a execption is costly ,

try:
    calculate_xfactor(-1)

except ValueError as error:
    print(error)
    # pass# pass and dont do anything
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return none
    return 10 / age
#rasie a execption is costly ,

try:
    calculate_xfactor(-1)

except ValueError as error:
    print(error)
    # pass# pass and dont do anything
"""

print("age count: ", timeit(code1, number=10000))  # 10000 repeatation)
print("age count: ", timeit(code2, number=10000))  # 10000 repeatation)
