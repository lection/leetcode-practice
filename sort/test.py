from compare import practice
from compare import bubble
from compare import insertion
from compare import selection
from compare import merge
from compare import quick

# sort_fn = practice.sort_fn
# sort_fn = bubble.bubble_sort
# sort_fn = insertion.insertion_sort
# sort_fn = selection.selection_sort
# sort_fn = merge.merge_sort
sort_fn = quick.quick_sort

cases = [
    [1, 1, 3, 5, 8, 9],
    [4, 5, 3, 6, 7, 5, 1],
    [3, 2, 7, 7, 6, 4, 5],
]

for case in cases:
    result = sorted(case)
    sort_fn(case)
    print(result == case)
