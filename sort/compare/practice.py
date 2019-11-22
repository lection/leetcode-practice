def sort_fn(array):
    if not array:
        return
    for i in range(0, len(array) - 1):
        min_index = i
        v = array[i]
        for j in range(i + 1, len(array)):
            if v > array[j]:
                min_index = j
                v = array[j]
        array[i], array[min_index] = array[min_index], array[i]
