"""
两个有序数组合并是非常简单高效的 分治法将整个数组拆成两份
O(n * log(n))
"""

def merge_sort(array):
    if not array:
        return

    length = len(array)
    if length == 1:
        return array

    half = length // 2
    arr1 = merge_sort(array[:half])
    arr2 = merge_sort(array[half:])

    li = ri = idx = 0
    while li < len(arr1) and ri < len(arr2):
        if arr1[li] <= arr2[ri]:
            array[idx] = arr1[li]
            li += 1
        else:
            array[idx] = arr2[ri]
            ri += 1
        idx += 1
    if li < ri:
        arr2 = arr1
        ri = li
    for i in range(ri, len(arr2)):
        array[idx] = arr2[i]
        idx += 1

    return array
