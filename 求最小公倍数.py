# 辗转bai相除法， 又名欧几里德算法（Euclidean algorithm），是求最大公约数的一种方法。
# 利用 gcd∗lcm = a∗b 求lcm
def gcd(a, b):
    while b:
        # 利用辗转相除法 greatest common divisor
        a, b = b, a % b
        pass
    return a


while True:
    try:
        # x = input().strip().split()
        # a1 = int(x[0])
        # b1 = int(x[1])
        # print(a1*b1//gcd(a1, b1))

        a1, b1 = map(int, input().split())
        print(a1*b1 // gcd(a1, b1))
    except:
        break