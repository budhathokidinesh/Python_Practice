def fizzbuzz(n):
    result = []

    for i in range(1, n+1):
        if i % 4 == 0 and i % 6 == 0:
            result.append("FizzBuzz")
        elif i % 4 == 0:
            result.append("Fizz")
        elif i % 6 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
print(fizzbuzz(20))