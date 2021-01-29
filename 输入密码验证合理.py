import re

x = '123123123abcdabcd'
x1 = re.findall(r'(.{3,}).*\1', x)
x2 = re.findall(r'[a-z]', x)
print(x1)
print(x2)


# try:
#     while True:
#         s = input()
#
#         a1 = re.findall(r'\d', s)
#         a2 = re.findall(r'[a-z]', s)
#         a3 = re.findall(r'[A-Z]', s)
#         a4 = re.findall(r'[^0-9A-Za-z]', s)
#
#         b = re.findall(r'(.{3,}).*\1', s)
#
#         if [a1, a2, a3, a4].count([]) <= 1 and b == [] and len(s) > 8:
#             print('OK')
#         else:
#             print('NG')
#
# except:
#     pass

