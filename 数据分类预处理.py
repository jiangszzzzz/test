# 字符串输出的排序

# # 字符串序列join
# str1 = "-"
# seq = ("a", "b", "c")
# print(str1.join(seq))
# a = ['1', '200', '14', '5', '21', '3', '2', '1']
# b = " "
# print(a)
# print(b.join(a))
# map 迭代
# a = list(set(map(int, a[1:])))
# a.sort()
# c = ''
# for i in a:
#     c += ' ' + str(i)
# print(c[1:])

# enumerate
# a = ['a', 'b', 'c']
# for i, sub in enumerate(a):
#     print(i, sub)

## list.append(object) 向列表中添加一个对象object
## list.extend(sequence) 把一个序列seq的内容添加到列表中


while True:
    try:
        s1 = input().split()[1:]
        s2 = list(set(map(int, input().split()[1:])))
        s2.sort()
        rst = []
        for num in s2:
            tmp = []
            for i, sub in enumerate(s1):
                if str(num) in sub:
                    tmp.extend([str(i), str(sub)])
            if tmp:
                rst.extend([str(num), str(len(tmp)//2)] + tmp)
        print(str(len(rst)) + ' ' + ' '.join(rst))
    except:
        break









