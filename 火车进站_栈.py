# 输入：
# 3
# 1 2 3
# 输出：
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 2 1
# 第一种方案：1进、1出、2进、2出、3进、3出
# 第二种方案：1进、1出、2进、3进、3出、2出
# 第三种方案：1进、2进、2出、1出、3进、3出
# 第四种方案：1进、2进、2出、3进、3出、1出
# 第五种方案：1进、2进、3进、3出、2出、1出
# 请注意，[3,1,2]这个序列是不可能实现的。

# 递归实现 栈

while True:
    try:
        n = int(input())
        a = input().split()
        res = []

        def rec_train(pre_train, in_train, out_train):
            """
            :param pre_train:  准备进站列表
            :param in_train: 已经进站列表
            :param out_train: 已经出站列表
            :return: 所有出站情况汇总
            rec_train() 单次进栈出站时调用一次
            """
            if not pre_train:
                # 准备进栈的列表为空 此时 只能出站
                # 出、进站列表 从左至右为 先后进、出顺序
                # 所以 out 不变 ，由于栈遵循 先进后原则 所以 in 必须倒序 然后加到 out之后
                # 此条件可以得到出站列表 为 递归出口
                res.append(' '.join(out_train + in_train[::-1]))
                return
            elif not in_train:
                # 进栈列表为空 此时 只能进栈
                # pre 切去第一个 放入 in， out不变
                rec_train(pre_train[1:], [pre_train[0]], out_train)
            else:
                # 其他情况 都可以进栈和出栈
                # 进栈
                rec_train(pre_train[1:], in_train + [pre_train[0]], out_train)
                # 出栈
                rec_train(pre_train, in_train[0:-1], out_train + [in_train[0]])
            return

        rec_train(a, [], [])
        res.sort()
        print('\n'.join(res))

    except:
        break