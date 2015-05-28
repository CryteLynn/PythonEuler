def sum_squares(num):
    """Returns the sum of the squares of all real numbers up to and
    including the given number."""

    return sum([x ** 2 for x in xrange(1, num + 1)])


def squared_sum(num):
    """Returns the square of the sum of all real numbers up to and
    including the given number."""

    return sum([x for x in xrange(1, num + 1)]) ** 2


def diff(num):
    """Returns the difference between the sum of squares and the
    square of the sum for all real numbers up to and including
    the given number."""

    return abs(squared_sum(num) - sum_squares(num))

print diff(100)
