# 问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
# 要求：
# 实现如下2个通配符：
# *：匹配0个或以上的字符（字符由英文字母和数字0-9组成，不区分大小写。下同）
# ？：匹配1个字符


# te?t*.*
# txt12.xls     text12.xls
# 输出 false


while True:
    try:
        a = input()
        b = input()   # a 长度必小于等于 b
        x = 0
        y = 0
        k = 1
        while x < len(a) and y < len(b):
            if a[x] == b[y] or a[x] == '?':
                x = x + 1
                y = y + 1
            elif a[x] == '*':
                if x == len(a) - 1 or y == len(b) - 1:
                    x = x + 1
                    y = y + 1
                    continue
                if a[x+1] == b[y+1]:
                    x = x + 1
                    y = y + 1
                else:
                    y = y + 1
            else:
                k = 0
                break
        if k == 1:
            print('true')
        else:
            print('false')
    except:
        break