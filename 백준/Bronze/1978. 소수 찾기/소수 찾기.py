n = int(input())
data = list(map(int, input().split()))
answer = 0 

for i in data: 
    cnt = 0 
    if i > 1:
        for j in range(2, i): 
            if i % j == 0: 
                cnt = 1 
                break
        if cnt == 0: 
            answer += 1

print(answer)