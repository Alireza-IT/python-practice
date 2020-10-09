try:
    with open("app.py") as file, open("another.txt") as target:  # auotmatically realase the resources
        # work with file obj
        print("file opened: ")
        file.__enter__  # magic function controls the context management protocl
        # if obj have these magic fun we can use with
    age = int(input("Age: "))
    xfactor = 10 / age

except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown.")

finally:  # always execurte
    file.close()
