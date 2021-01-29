a = 'aabbccc'
b = []
c = ''

for i in range(len(a)):
    b.append(a.count(a[i]))
for i in range(len(a)):
    if b[i] != min(b):
        c += a[i]
print(c)