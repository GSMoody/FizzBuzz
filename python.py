import sys
def FizzBuzz(x):
    result = []
    if x % 3 == 0:
        result.append("Fizz")
    if x % 5 == 0:
        result.append("Buzz")
    if x % 7 == 0:
        result.append("Bang")
    if x % 11 == 0:
        result = ["Bong"]
    if x % 13 == 0:
        if not result:
            result.append("Fezz")
        else:
            found = False
            for index in range(len(result)):
                if result[index][0] == "B":
                    result.insert(index, "Fezz")
                    found = True
                    break
            if not found:
                result.append("Fezz")
    if x % 17 == 0:
        result.reverse()
    if result:
        result = str(x) + ": " + "".join(result)
    else:
        result = x
    return (result)


option = input("Select option 1 for default, or option 2 for an individual number")
results = []
print(option)
if option == "1":
    for x in range(0, 301):
        result = FizzBuzz(x)
        print(result)
        results.append(result)
if option == "2":
    x = input("Enter integer for calculation")
    try:
        x = int(x)
    except ValueError:
        print("Please enter an integer")
        sys.exit()
    result = FizzBuzz(x)
    print(result)
else:
    print("Please enter '1' or '2'")
    sys.exit()