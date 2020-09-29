print("sending a message")


successful = False
for number in range(3):
    # for number in range(1, 4):
    print("sending a message", number, (number + 1) * ".")
    if successful:
        print("successful")
        break
else:
    print('attempted 3 times and then failed')
