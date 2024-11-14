def solution(s):
    answer = []
    zero = 0     
    change = 0
    
    
    while True:
        if s == "1":
            break;
            
        zero += s.count("0")  
        s = s.replace("0",'')    
        s = bin(len(s))[2:]     
        
        change += 1
        
    answer = [change, zero]    
    return answer