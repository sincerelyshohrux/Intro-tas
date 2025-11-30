def first_duplicate(x):
    seen = set()
    for num in x:
        if num in seen:
            return num
        seen.add(num)
    return -1


print(first_duplicate([1, 2, 3, 4, 2, 5]))  

