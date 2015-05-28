def find_pythagorean_triple_product(num):
    """Returns the product 'abc' for a pythagorean triple (a^2 + b^2 = c^2)
    whose sum a+b+c is equal to the given number. Utilizes Euclid's formula."""

    m = 2
    n = 1

    while True:
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2

        if a ** 2 + b ** 2 == c ** 2 and a + b + c == num:
            return a * b * c
        else:
            m += 1
            if m >= num:
                m = 1
                n += 1

print find_pythagorean_triple_product(1000)
