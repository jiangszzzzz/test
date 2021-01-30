# 斐波那契数列 1， 1， 2， 3， 5， 8， 13，21，34

while True:
    try:
        m = int(input())


# 递归公式 f(n) = f(n-1) + f(n-2)


        def foo(n):
            if n == 1 or n == 2:
                return 1
            elif n > 2:
                return foo(n-1) + foo(n-2)


        print(foo(m))

# 动态规划 k3 = k3 + k2
#        k2 = k1  ， k1 = k3

        k1 = 0
        k2 = 0
        k3 = 0
        for i in range(m):
            k3 = k3 + k2
            k2 = k1
            if k3 == 0 and k2 == 0:
                k1 = 1
            elif k3 == 0 and k2 == 1:
                k1 = 0
            else:
                k1 = k3
        print(k1 + k2 + k3)

    except:
        break

