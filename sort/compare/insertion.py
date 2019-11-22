"""
思路是在有序数组中插入一个元素 从后向前迭代并移动数据 直至移动到插入位置
将要排序的数组分成 已排序 和 未排序 两部分 迭代未排序 插入已排序
best: O(0)
avg: O(n^2)
bad: O(n^2)
"""

def insertion_sort(array):
    if not array:
        return
    for i in range(1, len(array)):
        v = array[i]
        j = i - 1
        while j >= 0:
            if v < array[j]:
                array[j + 1] = array[j]
            else:
                break
            j -= 1
        array[j + 1] = v
