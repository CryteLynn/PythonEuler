def numeric_palindrome(num):
    """Determines if the given number is a palindrome."""
    number = str(num)
    for x in xrange(len(number) / 2):
        if number[x] != number[(x + 1) * -1]:
            return False
    return True

palindromes = [x * y for x in xrange(100, 1000) for y in xrange(100, 1000) if numeric_palindrome(x * y)]

print max(palindromes)
