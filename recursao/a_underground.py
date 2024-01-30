def multOdd(number):
    result = 1
    if number <= 1:
        result = number
    elif not number % 2 == 0:
        result = number * multOdd(number - 2)
    else:
        result = multOdd(number - 1)
    return result
    
print(multOdd(int(input())))