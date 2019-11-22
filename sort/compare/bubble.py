"""
相邻两个交换 一次迭代将最大的放到最后
best: O(0)
avg: O(n^2)
bad: O(n^2)
"""

def bubble_sort(array):
    if not array:
        return
    for i in range(len(array)):
        flag = True
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                flag = False
                array[j], array[j + 1] = array[j + 1], array[j]

        if flag:
            return
