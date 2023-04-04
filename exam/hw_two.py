a = input()
b = input()
count = 0
i = 0
occupy = []
while i < len(a):
    for x in occupy:
        if a[i] == x:
            continue
    l = 0
    k = i
    if a[i] == b[0]:
        for j in range(len(b)):
            while k < len(a):
                if a[k] == b[j]:
                    l = l + 1
                    occupy.append(k)
                    k = k + 1
                    if j == len(b) - 1 and l == len(b):
                        count = count + 1
                    break
                else:
                    k = k + 1
    
    i = i + 1
print(count)

