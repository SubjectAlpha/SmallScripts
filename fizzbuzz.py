for i in range(1,101):
    output = ""
    divisibleBy3 = i % 3 == 0
    divisibleBy5 = i % 5 == 0
    if divisibleBy3 or divisibleBy5:
        if divisibleBy3:
            output += "Fizz"

        if divisibleBy5:
            output += "Buzz"
    else:
        output = i

    print(output)