for x in range(1,101):
    result=[]
    result=x
    if x % 3 == 0 and x % 5 != 0:
        result = "Fizz"
    if x % 5 == 0 and x % 3 != 0:
        result = "Buzz"
    if x % 5 == 0 and x % 3 == 0:
        result = "FizzBuzz"
    if x % 7 == 0 and not isinstance(result, str):
        result = "Bang"
    if x % 7 == 0 and isinstance(result, str):
        result = result+"Bang"
    if result == "BangBang":
        result = "Bang"
    if x % 11 == 0:
        result = "Bong"
    print(x, result)