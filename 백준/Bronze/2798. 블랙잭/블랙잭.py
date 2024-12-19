n, m = map(int, input().split())
nums = list(map(int, input().split()))
li = []
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            three = nums[i] + nums[j] + nums[k]
            if three > m:
                continue
            else:
                li.append(three)
print(max(li))