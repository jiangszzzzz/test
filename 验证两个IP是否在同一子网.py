# 判断ip与mask的合法性 然后 and 计算
# 输出 ‘0’ 为同一子网 ‘2’ 为不同子网 ‘1’为非法ip或mask

def is_ip(ip):
    rst = ''
    if len(ip) != 4:
        return False
    for i in ip:
        if 0 <= int(i) <= 255:
            rst += bin(int(i))[2:].rjust(8, '0')
        else:
            return False
    return rst


def is_mask(mask):
    rst = ''
    if len(mask) != 4:
        return False
    for i in mask:
        if 0 <= int(i) <= 255:
            rst += bin(int(i))[2:].rjust(8, '0')
        else:
            return False
    if '01' in rst or rst.startswith('0'):
        return False
    return rst


def ip_and_mask(ip, mask):
    res = ''
    for i in range(len(ip)):
        if ip[i] == '0' or mask[i] == '0':
            res += '0'
        else:
            res += '1'
    return res


while True:
    try:
        Mask = input().strip().split('.')
        Ip1 = input().strip().split('.')
        Ip2 = input().strip().split('.')

        mask1 = is_mask(Mask)
        ip1 = is_ip(Ip1)
        ip2 = is_ip(Ip2)

        if ip1 and ip2 and mask1:
            pass
        else:
            print('1')
            continue

        if ip_and_mask(ip1, mask1) == ip_and_mask(ip2, mask1):
            a = '0'
        else:
            a = '2'
        print(a)
    except:
        break