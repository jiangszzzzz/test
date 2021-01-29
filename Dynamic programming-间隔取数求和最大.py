import  numpy as np

arr1 = [1, 2, 3, 4, 3, 2, 1, 9]

# for循环 间隔取数，求和最大问题


def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        a = opt[i-2] + arr[i]
        b = opt[i-1]
        opt[i] = max(a, b)
    return opt[i]


print(int(dp_opt(arr1)))

# 递归


def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr1[0], arr1[1])
    else:
        a = rec_opt(arr, i-1)
        b = rec_opt(arr, i-2) + arr[i]
        return max(a, b)


print(rec_opt(arr1, (len(arr1)-1)))
