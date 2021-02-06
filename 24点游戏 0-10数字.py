#  输入四个0-10的数字 输出能否组成24点
#  思路是 利用递归反推

def helper(arr, item):
    # if item < 1:
    #     return False
    if len(arr) == 1:
        return arr[0] == item
    for i in range(len(arr)):
        L = arr[:i] + arr[i+1:]
        v = arr[i]
        if helper(L, item - v):
            return True
        elif helper(L, item + v):
            return True
        elif helper(L, item * v):
            return True
        elif helper(L, item / v):
            return True


while True:
    try:
        a = list(map(int, input().split()))
        if helper(a, 24):
            print('true')
        else:
            print('false')
    except:
        break