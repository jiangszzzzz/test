# 请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）沿着各自边缘线从左上角走到右下角，总共有多少种走法，
# 要求不能走回头路，即：只能往右和往下走，不能往左和往上走。

# 输入 m, n 方格行数列数

while True:
    try:
        m, n = map(int, input().split())

        def walk(x, y):
            """
            递归 当x或者y为0 为边界条件 返回 1
            :param x: 坐标
            :param y:
            :return: 返回可能的次数
            """
            if x == 0 or y == 0:
                return 1
            else:
                return walk(x-1, y) + walk(x, y-1)

        print(walk(m, n))
    except:
        break