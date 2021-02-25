# 计算两个字符串之间的距离，Levenshtein 距离，又称编辑距离
# 利用动态规划的方法
# 动态规划表 创建两个list dp[-1] 行 为最终需要的返回值 pre为列
# 第一行为：dp = [0 1 2 3] 第一列为 pre = [0 1 2]


def compare(a, b):
    m, n = len(a), len(b)
    dp = list(range(0, m+1))
    for i in range(1, n+1):
        pre = list(range(0, n+1))
        for j in range(1, m+1):
            t = dp[j]
            if a[j-1] == b[i-1]:
                dp[j] = pre[i-1]
            else:
                dp[j] = min(dp[j], pre[i], pre[i-1]) + 1
            pre[i] = dp[j]
            pre[i-1] = t
    res = dp[-1]
    return res


while True:
    try:
        a = input()
        b = input()
        if a == '' or b == '':
            print(max(len(a), len(b)))
        else:
            print(compare(a, b))
    except:
        break