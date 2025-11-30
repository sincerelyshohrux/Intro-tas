def find_factors(x):
    factors = []
    
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    
    return factors


x = 12
result = find_factors(x)
print(f"Factors of {x}: {result}")