# mp3 显示问题 输入1 全部歌曲个数 输入2 UD 操作字符串 输出当前页面页面（4） 输出当前光标

while True:
    try:
        num = int(input())
        s = input()
        n = 1   # 当前光标为n
        t = 1   # 当前目录的起点为 t
        res = ''
        for i in s:
            # 首先计算光标n的位置
            if i == 'U':
                n = n - 1
            else:
                n = n + 1
            if n < 1:
                n = num
            if n > num:
                n = 1
            # 计算当前的t的值 分为三种情况
            # 第一种：只会在 u 的情况产生 n<t t=n
            # 第二种：只会在 D 的情况产生 n>t+3 t = n - 3
            # 第三种： t=< n =< t + 3   t 维持不变
            if n < t:
                t = n
            if n > t + 3:
                t = n - 3
        for j in range(0, min(num, 4)):
            res += str(t + j) + ' '
        print(res)
        print(n)
    except:
        break