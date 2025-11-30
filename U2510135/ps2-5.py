def recursive_list_sum(new):
    total = 0
    for element in new:
        if isinstance(element, list):
            total += recursive_list_sum(element)
        else:
            total += element
    return total


result = recursive_list_sum([1, 2, [3, 4], [5, 6]])
print(result)





