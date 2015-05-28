def prime_factors(num):

    factors = []
    div = 2
    
    while num > 1:
        while num % div == 0:
            factors.append(div)
            num /= div
        div += 1
        
    return factors

print max(prime_factors(600851475143))
