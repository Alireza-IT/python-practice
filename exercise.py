def fizz_buzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "fizz"
    # else:
        # return  "buzz"
    # or
    if input % 5 == 0:  # we know that above if get falase get here
        return "buzz"
    return input


print(fizz_buzz(7))
