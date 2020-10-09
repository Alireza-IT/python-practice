# numbers = [1, 2]
# print(numbers[3])
# exceptio n is error that terminate the running the programs

try:
    age = int(input("Age: "))
except ValueError as error:
    print("You didn't enter a valid age.")
    print(error)
    print(type(error))  # show type of value error
else:
    print("no execption were thrown")  # only when we have no execptions
print("execution continues.")
