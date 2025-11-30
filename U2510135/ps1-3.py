def horner(a, x):
    if len(a) == 1:
        return a[0]
    return a[0] + x * horner(a[1:], x)
print(horner([3, 2, 1], 2)) 