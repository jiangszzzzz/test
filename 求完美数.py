# 求完全数 例如 28 其约数为1 2 4 7 14 28  1+2++4+7+14 = 28 除自身之外的约数和其自身
# 计算范围为500000
# 方法一 先找出500000 内的所有完全数

# res = list()
# for i in range(1, 50000):
#     sum1 = 0
#     a = list()
#     for j in range(1, i+1):
#         if i % j == 0:
#             a.append(j)
#     for x in a:
#         sum1 += x
#     if sum1 == i*2:
#         res.append(i)
# print(res)

# 输出为 [6, 28, 496, 8128]

#  ## 直接输出的方法
# while True:
#     try:
#         n = int(input())
#         m = 0
#         res = [6, 28, 496, 8128]
#         for y in res:
#             if n >= y:
#                 m += 1
#         print(m)
#     except:
#         break


##
while True:
    try:
        n = int(input())
        res = list()
        for i in range(2, n):
            a = list()
            for j in range(2, int(pow(i, 1/2)) + 1):
                if i % j == 0:
                    a.append(j)
                    a.append(i//j)
                    if sum(a) > i:
                        break
            if sum(a) + 1 == i:
                res.append(i)
        print(res)
    except:
        break



