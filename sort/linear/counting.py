"""
计数排序 更具体的桶排序
"""


def counting_sort(nums):
    if not nums:
        return
    # 界定上下限
    lower_limit = upper_limit = nums[0]
    for n in nums:
        if n > upper_limit:
            upper_limit = n
        elif n < lower_limit:
            lower_limit = n

    c = [0 for _ in range(upper_limit - lower_limit + 1)]

    for n in nums:
        c[n - lower_limit] += 1

    # 计数排序的核心部分
    # 定位排序结果依赖累加的计数数组
    for i in range(1, len(c)):
        c[i] += c[i - 1]

    copy = [n for n in nums]
    for n in copy:
        idx = n - lower_limit
        nums[c[idx] - 1] = n
        c[idx] -= 1
