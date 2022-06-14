def fizzbuzz(num):
    if num % 15 == 0:
        ret = 'FizzBuzz'
    elif num % 3 == 0:
        ret = 'Fizz'
    elif num % 5 == 0:
        ret = 'Buzz'
    else:
        ret = str(num)
    return ret
