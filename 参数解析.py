# 在命令行输入如下命令：
#
# xcopy /s c:\ d:\
# xcopy /s  "C:\program files" "d:\"
#
# 各个参数如下：
# 参数1：命令字xcopy
# 参数2：字符串 /s
# 参数3：字符串c:\
# 参数4: 字符串d:\
# 请编写一个参数解析程序，实现将命令行各个参数解析出来。

# 解析规则：
#
# 1.参数分隔符为空格
# 2.对于用“”包含起来的参数，如果中间有空格，不能解析为多个参数。比如在命令行输入xcopy / s “C:\program files” “d:\”时，
# 参数仍然是4个，第3个参数应该是字符串C:\program files，而不是C:\program，注意输出参数时，需要将“”去掉，引号不存在嵌套情况。
# 3. 参数不定长
# 4. 输入由用例保证，不会出现不符合要求的输入


# 利用flag 区分普通空格 和 “ ”中的空格

while True:
    try:
        s = input()
        res = ''
        flag = 0
        list1 = []
        for i in range(len(s)):
            if s[i] == ' ' and flag == 0:  # 字符串遍历 出现空格时 为一条命令 flag=0 表示 非“ ”中的空格
                if res != '':    # “ ”之后的空格的情况 此时res = '' 所以不执行append
                    list1.append(res)
                    res = ''
                continue
            if s[i] == ' ' and flag == 1:  # “ ”中的空格执行 res += s[i]
                pass
            if s[i] == '"' and flag == 0:  # 第一个“ 设置 flag 为 1
                flag = 1
                continue
            if s[i] == '"' and flag == 1:
                list1.append(res)
                res = ''
                flag = 0    # 第二个“ 设置 flag 为 0
                continue
            else:
                res += s[i]
                if i == len(s)-1:  # 字符串末尾无空格
                    list1.append(res)
        print(len(list1))
        for j in list1:
            print(j)
    except:
        break