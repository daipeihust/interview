a = list(input())
mark = list()
nums = list()
strs = list()
result = list()
for i in range(len(a)):
    if '0' <= a[i] <= '9':
        strs.append(a[i])
    else:
        mark.append(i)
        nums.append(a[i])
nums.sort()
strs.sort()
j = 0
k = 0
for i in range(len(a)):
    if i in mark:
        result.append(nums[j])
        j = j + 1
    else:
        result.append(strs[k])
        k = k + 1
print(result)


