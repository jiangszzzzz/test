# 输入整数 转换成二进制 输出 其中 1 的个数
# python 进制转化 十进制转换二进制bin() 十进制转换八进制 oct() 十进制转换十六进制 hex()
#  其他进制转换成 十进制    二转十 int('ob100', 2)  八转十 int('0o04' ,8)  十六转十 int('0x4',16)


while True:
    try:
        a = int(input())
        b = list(bin(a))
        n = 0
        for i in b:
            if i == '1':
                n = n +1
        print(n)
    except:
        break