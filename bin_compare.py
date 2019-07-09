a = '10100001'
b = '10100011'
c = ''

a1 = [i for i in a]
b1 = [i for i in b]

for i in range(len(a)):
    if a1[i] == b1[i] == '1':
        c += '1'
    else:
        c += '0'

print(a)
print(b)
print(c)