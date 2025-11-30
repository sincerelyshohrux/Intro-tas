def element_frequency(x):
    new = {}
    for num in x:
        new[num] = new.get(num, 0) + 1
    
    result = {}
    for i in range(10):
        result[i] = new.get(i, 0)
    
    return result


result = element_frequency([2, 1, 2, 3, 1, 9])
print(result)