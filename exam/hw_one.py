line = set(input())
n = int(input())
line.remove('[')
line.remove(']')
if len(line) >= 4:
    line.remove(',')
    line.remove(' ')

ava = []
for i in line:
    ava.append(int(i))
num1 = 0
num2 = 0
for i in ava:
    if i < 4:
        num1 = num1 + 1
    else:
        num2 = num2 + 1
result = []
if num1 > 0 or num2 > 0:
    if n == 1:
        if num1 == num2:
            for i in ava:
                if i >= 4:
                    result.append(i)    
            for i in ava:
                result.append([i])
        elif num1 == 1:
            for i in ava:
                if i < 4:
                    result.append([i])
        elif num2 == 1:
            for i in ava:
                if i >= 4:
                    result.append([i])
        elif num1 == 3:
            for i in ava:
                if i < 4:
                    result.append([i])
        elif num2 == 3:
            for i in ava:
                if i >= 4:
                    result.append([i])
        elif num1 == 2:
            for i in ava:
                if i < 4:
                    result.append([i])
        elif num2 == 2:
            for i in ava:
                if i >= 4:
                    result.append([i])
        else:
            for i in ava:
                result.append([i])
    elif n == 2:
        if num1 == num1 and num1 >= 2:
            for i in range(len(ava)):
                j = i + 1
                tmp1 = []
                tmp2 = []
                while j < len(ava):
                    if ava[i] < 4 and ava[j] < 4:
                        tmp1.append(ava[i])
                        tmp1.append(ava[j])
                    elif ava[i] >= 4 and ava[j] >= 4:
                        tmp2.append[ava[i]]
                        tmp2.append[ava[j]]
                if len(tmp1) > 0:
                    result.append(tmp1)
                if len(tmp2) > 0:
                    result.append(tmp2)
        elif num1 == 2:
            tmp = []
            for i in ava:
                if i < 4:
                    tmp.append(i)
            result.append(tmp)
        elif num2 == 2:
            tmp = []
            for i in ava:
                if i >= 4:
                    tmp.append(i)
            result.append(tmp)
        elif num1 == 4:
            for i in range(len(ava)):
                j = i + 1
                tmp = []
                while j < len(ava):
                    if ava[i] < 4 and ava[j] < 4:
                        tmp.append(ava[i])
                        tmp.append(ava[j])
                result.append(tmp)
        elif num2 == 4:
            for i in range(len(ava)):
                j = i + 1
                tmp = []
                while j < len(ava):
                    if ava[i] >= 4 and ava[j] >= 4:
                        tmp.append(ava[i])
                        tmp.append(ava[j])
                result.append(tmp)
        elif num1 == 3:
            for i in range(len(ava)):
                j = i + 1
                tmp = []
                while j < len(ava):
                    if ava[i] < 4 and ava[j] < 4:
                        tmp.append(ava[i])
                        tmp.append(ava[j])
                result.append(tmp)
        elif num2 == 3:
            for i in range(len(ava)):
                j = i + 1
                tmp = []
                while j < len(ava):
                    if ava[i] >= 4 and ava[j] >= 4:
                        tmp.append(ava[i])
                        tmp.append(ava[j])
                result.append(tmp)
    elif n == 4:
        if num1 == 4 and num2 == 4:
            result = [[0, 1, 2, 3], [4, 5, 6, 7]]
        elif num1 == 4:
            result = [[0, 1, 2, 3]]
        elif num2 == 4:
            result = [[4, 5, 6, 7]]
    elif n == 8:
        if num1 == 8 and num2 == 8:
            result = [[0, 1, 2, 3 ,4, 5, 6, 7]]
print(result)



