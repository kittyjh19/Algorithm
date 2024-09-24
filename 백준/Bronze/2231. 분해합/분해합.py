n = int(input()) # 입력 값(n) 받기
answer = 0 # 결과를 담을 변수를 생성(answer)

for i in range(1, n+1): # for문으로 1부터 n까지 모든 수를 계산해 분해합 구하기
    nums = list(map(int, str(i)))
    answer = sum(nums) + i
    if answer == n:
        print(i)
        break
    if i == n:
        print(0)
