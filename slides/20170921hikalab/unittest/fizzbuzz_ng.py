def fizzbuzz(num):
    if num % 3 == 0:
        ret = 'Fizz'
    elif num % 5 == 0:
        ret = 'Buzz'
    elif num % 15 == 0:  # ここが間違い
        ret = 'FizzBuzz'
    else:
        ret = str(num)
    return ret

for num in range(1, 100):
    print(fizzbuzz(num))
