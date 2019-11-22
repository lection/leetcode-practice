"""
类似insertion 将数组分为 已排序 和 未排序两部分
在未排序中查找最小值 插入已排序的末尾 也就是跟未排序的第一个元素交换
best: O(n^2)
avg: O(n^2)
bad: O(n^2)
"""
def selection_sort(array):
    if not array:
        return
    for i in range(len(array) - 1):
        v = array[i]
        min_idx = i
        for j in range(i + 1, len(array)):
            if v > array[j]:
                min_idx = j
                v = array[j]
        array[i], array[min_idx] = array[min_idx], array[i]
