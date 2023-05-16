a = list(0 for i in range(26))
for i in a:
    a[ord(i)-65] = a[ord(i)-65] + 1
num = max(a)
if a.count(num) >= 2:
    print('?')
else:
    print(chr(a.index(num) + 65))