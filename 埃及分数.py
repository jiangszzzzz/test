# 分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。如：8/11 = 1/2+1/5+1/55+1/110。
# 注：真分数指分子小于分母的分数，分子和分母有可能gcd不为1！
# 如有多个解，请输出任意一个。

# a,b互质，其中a<b,则可以进行如此的拆分  b=a*p+r
# p+1 作为分母
# https://blog.nowcoder.net/n/8ab21466ce9a4a18b289d31a50b8cb7b?f=comment
while 1:
    try:
        a, b = map(int, input().split('/'))
        res = []
        while 1:
            if a == 1 or b % a == 0:    # 当 a=1 或者 b%a=0 为函数出口
                res.append('1' + '/' + str(b//a))
                break
            else:
                p = int(b/a)
                r = b % a
                b = (p + 1)*(a*p + r)  # 新的b 求b时需要当前的a 所以 b在前
                a = a - r  # 新的a
                res.append('1' + '/' + str(p+1))
        print('+'.join(res))
    except:
        break