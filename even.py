#code challenge
import random

start = 5


def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2

while start:
    num = random.randint(1, 99)
    even_odd(num)
    if num % 2 == 0:
        print("{} is even".format(num))
    else:
        print("{} is odd".format(num))
    start = start -1    