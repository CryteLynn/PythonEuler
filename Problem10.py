from math import sqrt

def prime(num):
    """Returns True if num is prime, False if not."""

    for x in xrange(2, int(sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

print sum([y for y in xrange(2, 2000000) if prime(y)])
