def Solution(a, b, c):
  sides = sorted([a, b, c])
  return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

while True:
  a, b, c = map(int, input().split())
  if a == 0 and b == 0 and c == 0:
    break

  if Solution(a, b, c):
    print("right")
  else:
    print("wrong")