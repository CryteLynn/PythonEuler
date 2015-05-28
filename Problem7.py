def prime(num):
    """Determines if a number is prime."""
    for x in xrange(2, num):
        if num % x == 0:
            return False
    return True


def find_nth_prime(n):
    """Returns the nth prime number."""

    x = 1
    num = 2
    while x != n:
        num += 1
        if prime(num):
            x += 1
        print x, num
    return num

print find_nth_prime(10001)
