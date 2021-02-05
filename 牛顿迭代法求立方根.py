# 牛顿迭代法 求解立方根
# 迭代公式 为  Xk+1 = Xk - f(Xk)/f'(Xk)
# while abs(f(x)) > 1e-7 可能为负数 所以要求绝对值
# x = 1 为初始值 表示 求解在x = 1 附近的根
# round(x, 1) 保留一位小数

while True:
    try:
        n = float(input())
        x = 1
        while abs(x**3 - n) > 1e-7:
            x = x - (x**3 - n)/(3*x**2)
        print(round(x, 1))
    except:
        break