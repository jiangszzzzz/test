# 编写一个程序，将输入字符串中的字符按如下规则排序。
# 规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
# 如，输入： Type 输出： epTy
# 规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
# 如，输入： BabA 输出： aABb
# 规则 3 ：非英文字母的其它字符保持原来的位置。
# 如，输入： By?e 输出： Be?y

# 输入
# A Famous Saying: Much Ado About Nothing (2012/8).
# 输出
# A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).

while 1:
    try:
        s = input()
        p = []
        q = [False]*len(s)
        res = ''
        for i, v in enumerate(s):  # enumerate() i为标号 v 为值
            if v.isalpha():  # str.isalpha() 判断是否为字母
                p.append(v)
            else:
                q[i] = v
        p.sort(key=str.upper)  # 对p的字母排序 无视大小写 ，返回后的排序p值 大小写字母会按照输入先后顺序
        res = ''
        for j in q:
            if j:
                res += j
            else:
                res += p.pop(0)  # 每次移出 p 的第一个元素
        print(res)
    except:
        break