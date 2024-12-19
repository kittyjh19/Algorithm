L = int(input())
str = input()
mod = 1234567891
answer = 0

for i in range(L):
    answer += (ord(str[i]) - 96) * (31 ** i)
print(answer % mod)