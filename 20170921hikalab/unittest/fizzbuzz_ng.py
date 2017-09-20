def fizzbuzz(num):
    if num % 3 == 0:
        ret = 'Fizz'
    elif num % 5 == 0:
        ret = 'Buzz'
    elif num % 15 == 0:
        ret = 'FizzBuzz'
    else:
        ret = str(num)
    return ret
