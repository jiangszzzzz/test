# 华为oj 任意一个起点，从前到后，但只能从低处往高处的桩子走。他希望走的步数最多
# 求最长上升子序列
# bisect 用于二分搜索 1 返回位置 2 插入
# bisect.bisect(a, 13) 查询13在a中的位置
# bisect.bisect_left(a , 13) 查询13 插入到 a中的位置（如果相同则靠左插入）
# a.insert(pos, 13) 13插入到a的 pos 位置上 ------ bisect.insert(a, 13) 查询与插入

import bisect
while True:
    try:
        a = int(input())
        b = list(map(int, input().split()))
        q = []
        for v in b:
            pos = bisect.bisect_left(q, v)   # q 为最长上升子序列
            if pos == len(q):
                q.append(v)
            else:
                q[pos] = v
        print(len(q))
    except:
        break