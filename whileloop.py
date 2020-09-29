# iterate as long as condition is true

# number = 100

# while number > 0:
#     print(number)
#     number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print('ECHO', command)

# infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == 'quit':
        break
