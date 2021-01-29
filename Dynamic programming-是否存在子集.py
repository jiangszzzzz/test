arr1 = [3, 34, 4, 12, 5, 2]

import numpy as np
# 递归


def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr, i - 1, s)
    else:
        a = rec_subset(arr, i - 1, s - arr[i])
        b = rec_subset(arr, i - 1, s)
        return a or b


print(rec_subset(arr1, len(arr1) - 1, 1))
# print(rec_subset(arr1, len(arr1) - 1, 79))
# print(rec_subset(arr1, len(arr1) - 1, 1))

# 二维数组, 注意边界条件


def dp_subset(arr, s):
    subset = np.zeros((len(arr), s + 1), dtype=bool)
    subset[0, :] = False
    subset[:, 0] = True
    if s + 1 > arr[0]:
        subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, s+1):
            if arr[i] > s:
                subset[i, s] = subset[i-1, s]
            else:
                a = subset[i-1, s - arr[i]]
                b = subset[i-1, s]
                subset[i, s] = a or b
    r, c = subset.shape
    return subset[r-1, c-1]


print(dp_subset(arr1, 1))
print(dp_subset(arr1, 9))





