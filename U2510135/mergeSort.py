def mergeSort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

  
    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)

    
    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

  
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

   
    if left_idx < len(left):
        result.extend(left[left_idx:])

    if right_idx < len(right):
        result.extend(right[right_idx:])

    return result



nums = [3, 1, 4, 1,12,8,45,101, 5, 9, 2, 6, 3,8,100,5, 4]
print("Sorted result:", mergeSort(nums))