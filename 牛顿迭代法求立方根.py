# 牛顿迭代法 求解立方根
# 以 y = x**3 为例子
# fx = x**3 - y
# fx = 0 为需要求的点 及曲线与x轴交点
# 以 x1 为起点 此时 fx 在 x1 的切线为 y = fx1 + f'x1(x - x1)
# 切线与 x 轴交点为 （x1 - f(x1)/f'(x1)）
# 迭代上述步骤 直到切线交点 无限接近与 fx与x轴交点 
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
