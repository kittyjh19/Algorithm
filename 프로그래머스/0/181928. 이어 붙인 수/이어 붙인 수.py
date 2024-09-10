def solution(num_list):
    a = ''
    b = ''
    answer = 0
    
    for i in num_list:
        if i % 2 == 0:
            a += str(i)
        elif i % 2 == 1:
            b += str(i)
    answer = int(a) + int(b)
    return answer