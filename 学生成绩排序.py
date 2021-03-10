# 3 输入总人数
# 0 0代表从高到低，1代表从低到高
# fang 90 1
# yang 50 2
# ning 70 3
# 输出
# fang 90
# ning 70
# yang 50

# 测试用例中会出现 重名 与 重分 两种情况

while True:
    try:
        a = int(input())
        b = int(input())
        d = []  # 二维列表
        sc = []  # 成绩列表

        for i in range(a):
            c = list(input().split())
            d.append(c)    # 二维列表存放 成绩 与 名字
            sc.append(int(c[1]))  # 列表 用来排序的成绩

        if b == 0:
            bb = True
        else:
            bb = False

        t = sorted(sc, reverse=bb)

        for i in range(a):
            for j in range(a):
                if t[i] == int(d[j][1]):
                    res = d[j][0] + ' ' + d[j][1]
                    print(res)
                    res = ''
                    d[j][1] = '-1'   # 防止出现分数相同的情况
    except:
        break