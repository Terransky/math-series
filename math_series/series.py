a = 0
b = 1
c = -1
l = 2
counter = 2


def fibonacci(n):
    """It's technically recursion since I'm returning the function, but I feel like I cheated somehow
    by using global variables and counters. Could probably refactor to pass them in as arguments"""

    global a, b, c, counter
    c = a + b

    if n == 0:
        return a

    elif n == 1:
        return b

    elif n < 0:
        print("Please input a positive integer")

    elif counter == n:
        a, b, counter = 0, 1, 2
        return c

    else:
        a = b
        b = c
        counter += 1
        return fibonacci(n)


def lucas(n):
    """same function as fibonacci with different parameters"""

    global l, b, c, counter

    c = l + b

    if n == 0:
        return l

    elif n == 1:
        return b

    elif n < 0:
        print("Please input a positive integer")

    elif counter == n:
        l, b, counter = 2, 1, 2
        return c

    else:
        l = b
        b = c
        counter += 1
        return lucas(n)


def sum_series(n, x1=0, x2=1):
    """This functions accepts extra arguments to run any xn-1 + xn-2 series but Fibonacci by default"""

    global c, counter

    c = x1 + x2

    if n == 0:
        return x1

    elif n == 1:
        return x2

    elif n < 0:
        print("Please input a positive integer")

    elif counter == n:
        counter = 2
        return c

    else:
        x1 = x2
        x2 = c
        counter += 1
        return sum_series(n, x1, x2)


print("fib(7): ", fibonacci(7))
print("lucas(7): ", lucas(7))
print("sum series(7) default: ", sum_series(7))
print("sum series(7, 2, 1) lucas: ", sum_series(7, 2, 1))
print("sum series(7, 5, 4) random: ", sum_series(7, 5, 4))
