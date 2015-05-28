def fibonacci(max_value):

    a = 1
    b = 2
    fib_nums = []
    while b < max_value:
        fib_nums.append(a)
        a, b = b, a + b
    return fib_nums

print sum([x for x in fibonacci(4000000) if x % 2 == 0])
