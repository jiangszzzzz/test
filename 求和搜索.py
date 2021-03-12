# 输入int型数组，询问该数组能否分成两组，使得两组中各元素加起来的和相等，
# 并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），
# 能满足以上条件，输出true；不满足时输出false。


# 先将输入的数分在三个list里面 x y z
# 然后 在z中挑选元素放到 x y。 由于要求 最终 sum x = sum y
# 考虑 z中存在负数  负数加到 x 中 等于 负数的绝对值 加到 y 中
# 所以 z.append(abs(i))
# 此时只有考虑加的方向 判断 sum x ， sum y 中的小的那个 将 z 中元素加上
# 必须使用 z.sort(reverse=True) 小的放到后面加
while True:
    try:
        a = int(input())
        b = list(map(int, input().split()))
        x, y, z = [], [], []
        for i in b:
            if i % 5 == 0:
                x.append(i)
            elif i % 3 == 0:
                y.append(i)
            else:
                z.append(abs(i))
        z.sort(reverse=True)
        s5 = sum(x)
        s3 = sum(y)
        for j in z:
            if s5 < s3:
                s5 += j
            else:
                s3 += j
        print('true' if s5 == s3 else 'false')
    except:
        break