# 找出 ’G‘ ‘C’ 比例最高的子串,如果有多个输出第一个的子串
# 输入1 为字符串 输入2 为 子串长度

while True:
    try:
        s = list(input())    # 输入的字符串
        num = int(input())    # 输出子串的长度
        b = []      # 存放所有子串的 gc 比例
        res = ''    # 输出
        if len(s) <= num:   # 子串长度大于s 直接输出
            for k in s:
                res += k
            print(res)
        else:
            for j in range(0, len(s) - num):   # 从第一个子串开始计算各个子串的 GC 比例 放入b
                n = 0
                for i in range(0, num):
                    if s[i+j] == 'G' or s[i+j] == 'C':
                        n = n + 1
                b.append(n)
            c = max(b)
            for i in range(0, len(b) - 1):   # 从第一个开始找是否为最大值 如果是则输出子串 并且break
                if b[i] == c:
                    for j in range(0, num):
                        res += s[i+j]
                    print(res)
                    break
    except:
        break