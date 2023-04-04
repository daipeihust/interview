a = input()
b = input()
c = []
d = set()
count = 0
for i in range(len(b)):
    if b[i] != a:
        c.append(b[i])
        d.add(b[i])
for x in d:
    tmp = 0
    for y in c:
        if x == y:
            tmp = tmp + 1
    if tmp > 2:
        tmp = 2
    count = count + tmp
print(count)