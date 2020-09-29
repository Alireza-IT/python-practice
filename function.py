
def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome on board")


greet("Alireza", "Ashtari")


# 1-perform task
#

# 2-return a value
def get_greeting(name):
    return f"hi {name}"


message = get_greeting("alireza")
print(message)


def increment(number, value):
    return number * value


result = increment(2, 1)
print(result)
#
# print(increment(number=2,by=1))


# default argument
# def increment1(number, 1):
#     return number * value


# 5 goes and replace 1
# print(increment1(2, 5))

# xarg
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
# return a tuples

# xargs


def save_user(**user):
    print(user["name"])


save_user(id=1, name="alireza", age=22)
# return dictionary

# scope


def send_email(name):
    message = "b"
