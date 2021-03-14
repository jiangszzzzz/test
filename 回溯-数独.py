# 输入：
# 0 9 2 4 8 1 7 6 3
# 4 1 3 7 6 2 9 8 5
# 8 6 7 3 5 9 4 1 2
# 6 2 4 1 9 5 3 7 8
# 7 5 9 8 4 3 1 2 6
# 1 3 8 6 2 7 5 9 4
# 2 7 1 5 3 8 6 4 9
# 3 8 6 9 1 4 2 5 7
# 0 4 5 2 7 6 8 3 1

# 在 0 处填入 1-9
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

# 递归与回溯
# 回溯法标准框架：
#
# def backtrack(path, selected):
#     if 满足停止条件：
#         res.append(path)
#     for 选择 in 选择列表：
#         做出选择
#         递归执行backtrack
#         撤销选择

while 1:
    try:
        matrix = []
        for i in range(9):
            s = list(map(int, input().split()))
            matrix.append(s)      # 二维数组输入

        def solve(ma, count=0):  # count 遍历 数组的每个元素
            if count == 81:  # 递归出口
                return True
            row = count // 9  # 计算出当前的行标 列标
            col = count % 9
            if ma[row][col] != 0:  # 不为0 的 继续执行递归 遍历下一个元素
                return solve(ma, count=count + 1)
            for i1 in range(1, 10):  # 为0 for循环找合适的数
                if not check(ma, row, col, i1):  # 不合适继续
                    continue
                ma[row][col] = i1  # 找到符合要求的  做出选择 赋值                    选择
                if solve(ma, count=count + 1):   # 继续遍历下一个元素                递归执行
                    return True    # 如果后续 找到的所有 值都满足要求 则 返回True
                ma[row][col] = 0  # 如果后续 不符合要求 则 撤销上一步的选择 继续for循环    回溯
            return False  # 如果for循环中找不到符合要求的 则返回False 数独无解

        def check(ma, row, col, val):  # 注意此时的 ma[row][col] = 0
            for i2 in range(9):   # 判断则是的 矩阵中 行列中 是否有与val 相同的值  有则 check False
                if val == ma[row][i2]:
                    return False
                if val == ma[i2][col]:
                    return False
            row1 = (row // 3) * 3  # 找到所属 3*3 宫内的 左上角坐标
            col1 = (col // 3) * 3
            for j1 in range(3):
                for j2 in range(3):
                    if ma[row1+j1][col1+j2] == val:
                        return False
            return True

        solve(matrix)
        for i in range(9):
            print(' '.join(map(str, matrix[i])))
    except:
        break