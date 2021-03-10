# 连个输入字符串 求两个字符串的 最大公共子字符串
# 输入1 abcdefghijklmnop
# 输入2 abcsafjklmnopqrstuvw
# 输出 jklmnop


# 遍历方法 先找出 a 的所有子串 判断是否在b中 如果长度比当前res长 则更新 res
while True:
    try:
        a = input()
        b = input()
        res = ''
        if len(a) > len(b):
            a, b = b, a
        for i in range(len(a)+1):
            for j in range(len(a)+1):
                if a[i:j] in b and len(res) < j - i:
                    res = a[i:j]
        print(res)
    except:
        break


# 从a 的首字母开始 每次往后移一位 判断是否在b
# 是：res，n加1   n为当前子串的长度
# 否：i加一（从a第二个字母开始 长度为n 的子串开始查找）
while True:
    try:
        a = input()
        b = input()
        if len(a) > len(b):
            a, b = b, a
        res = ''
        i = 0
        n = 1
        while i + n <= len(a):
            if a[i:i+n] in b:
                res = a[i:i+n]
                n = n + 1
            else:
                i = i + 1
        print(res)
    except:
        break