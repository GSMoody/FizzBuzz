import sys
for x in range(1, 301):
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
        print(str(x) + ": " + "".join(result))
    else:
        print(x)
