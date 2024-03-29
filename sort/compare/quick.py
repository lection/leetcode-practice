"""
在数组中抽取一个数据pivot 将小于pivot的放在左边 大于的放在右边 以此分治
pivot 抽取方案很多 比如中间值 或末位置 或者随机抽取 或者随机抽取三个并选择中间值
先用最末尾的值做实验
"""

def quick_sort(array):

    def quick_fn(left, right):
        if left >= right:
            return
        pivot_idx = partition(left, right)
        quick_fn(left, pivot_idx - 1)
        quick_fn(pivot_idx + 1, right)

    # 各种pivot的抽取实现 并交换到right
    def extract_pivot(left, right):
        pass

    def partition(left, right):
        extract_pivot(left, right)
        pivot = array[right]
        idx = left
        for i in range(left, right):
            if array[i] < pivot:
                array[idx], array[i] = array[i], array[idx]
                idx += 1
        array[idx], array[right] = array[right], array[idx]
        return idx

    quick_fn(0, len(array) - 1)
