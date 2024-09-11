n = int(input())
for i in range(n):
  result = input()

  cnt = 0
  score = 0
  for j in result:
    if j == 'O':
      cnt += 1
    else:
      cnt = 0
    score += cnt
  print(score)