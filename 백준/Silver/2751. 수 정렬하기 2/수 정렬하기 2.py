import sys

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

for num in numbers:
    print(num)