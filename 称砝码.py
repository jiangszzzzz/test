# 输入
# 第一行：n --- 砝码数(范围[1,10])
#
# 第二行：m1 m2 m3 ... mn --- 每个砝码的重量(范围[1,2000])
#
# 第三行：x1 x2 x3 .... xn --- 每个砝码的数量(范围[1,6])

# 输出所有可能的重量

while 1:
    try:
        n = int(input())
        weight = list(map(int, input().split()))
        count = list(map(int, input().split()))
        fm, ans = [], {0}   # 砝码列表 和 所有可能重量的集合

        for i in range(n):   # 将所有砝码放入列表 [1,1,2] 表示 重量为1的砝码两个 重量为2的砝码一个
            for j in range(count[i]):
                fm.append(weight[i])

        for i in fm:  # 遍历砝码列表
            temp = list(ans)   # 当前可能的重量 起点为{0}
            for j in temp:     # 遍历当前的所有可能的重量 加上当前的砝码 i
                ans.add(j + i)   # 集合可以去重

        print(len(ans))
    except:
        break
