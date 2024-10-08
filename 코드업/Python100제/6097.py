h, w = map(int, input().split())
n = int(input())

m = []
for i in range(h + 1):
    m.append([])
    for j in range(w + 1):
        m[i].append(0)

for i in range(n):
    l, d, x, y = map(int, input().split())
    if int(d) == 0:
        for j in range(int(l)):
            m[int(x)][int(y) + j] = 1
    else:
        for j in range(int(l)):
            m[int(x) + j][int(y)] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(m[i][j], end=' ')
    print()
