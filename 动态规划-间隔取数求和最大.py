# 条件间隔取数字，求取数的最大和
import numpy as np

arr1 = [1, 2, 3, 4, 3, 2, 1, 9]
# 递归方法
# i = 0, 只能选arr[0]
# i = 1, 选arr[0] 与arr[1] 中最大的
# 递归问题 第i个选或者不选 不选：a  rec_opt(arr, i-1) 选：b rec_opt(arr, i-2) + arr[i]
# i = 2 时 递归出口为 max（a,b）。。。


def rec_opt(arr, i):
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr1[0], arr1[1])
    else:
        a = rec_opt(arr, i - 1)
        b = rec_opt(arr, i - 2) + arr[i]
        return max(a, b)


print(rec_opt(arr1, (len(arr1) - 1)))

# 先生成opt数组 np.zeros(len(arr))
# opt[0] = arr[0] opt[1] = max(arr[0], arr[1])
# opt[2] : 选或者不选 a，b 两种情况 i = 2 时 for循环一次
# opt[3] : for循环 利用上一步计算opt[2] 计算 opt[3]..opt[i] 为最终输出


def dp_opt(arr):
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        a = opt[i - 2] + arr[i]
        b = opt[i - 1]
        opt[i] = max(a, b)
    return opt[len(arr) - 1]


print(int(dp_opt(arr1)))
