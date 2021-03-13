# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
#
# 所有的小写字母在大写字母前面
#
# 所有的字母在数字前面
#
# 所有的奇数在偶数前面

s = 'Sorting1234'
s1 = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x.islower(), x))
print(''.join(s1))

# 输出为
# ginortS1324

# key 用来决定在排序算法中 cmp 比较的内容，key 可以是任何可被比较的内容，比如元组（python 中元组是可被比较的）
# 这里，lambda 函数将输入的字符转换为一个元组，然后 sorted 函数将根据元组（而不是字符）来进行比较，进而判断每个字符的前后顺序。

# x.isdigit() 返回 True 和 False ， False在前 所以x.isdigit() 为数字在后
# x.isdigit() and int(x) % 2 == 0 同理 偶数在后
# x.isupper(), x.islower() 同理为大写在后 和小写在后 但是 x.isupper() 在前面 所以大写在后
# x 为 Ascll码排序
# 排序的结果 满足上述条件 然后输出