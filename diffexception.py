try:
    file = open("app.py")  # return file obj
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
# except ZeroDivisionError:
#     print("age can not be zero")
    # print("You didn't enter a valid age") # looks ygly
else:
    print("No exceptions were thrown.")

finally:  # always execurte
    file.close()
