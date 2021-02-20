# python list.sort()方法仅被定义在list， 相反地sorted()方法对所有的可迭代序列都有效。
# sorted 为简单的升序排序 返回一个新的list
# https://www.cnblogs.com/wjw2018/p/10613242.html

while True:
    try:
        a = input()
        s = list(set(a))  # 集合去重复
        d = {}   # 定义字典
        r = ''
        # 字符出现的次数为字典的key value为字符或 字符串
        for i in s:
            if a.count(i) not in d:
                d[a.count(i)] = ''
            d[a.count(i)] += i
        t = sorted(d, reverse=True)  # 先对出现次数排序 对字典的key值 排序
        for j in t:
            r += ''.join(sorted(d[j]))  # 对字典的value值进行ASCII码排序
        print(r)
    except:
        break

