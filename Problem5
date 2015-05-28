def lowest_common_multiple(m):
    """Returns the smallest number evenly divisible by all numbers
    up to and including the given argument."""
    
    a = m
    start = 2
    while (m % start) == 0:
        start += 1

    b = start
    while b < m:
        if ( a % b) != 0:
            a += m
            b = start
        else:
            b += 1
    return a

print lowest_common_multiple(20)
