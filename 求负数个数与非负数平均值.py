a = 0
b = 0
c = 0
while True:
    # noinspection PyBroadException
    try:
        x = int(input())
        if x >= 0:
            a += x
            b += 1
        else:
            c += 1
    except:
        break

print(c)
if b > 0:
    print(round(a/b, 1))
else:
    print(0.0)