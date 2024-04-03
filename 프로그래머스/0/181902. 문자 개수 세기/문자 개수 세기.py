def solution(my_string):
    answer = [0 for i in range(52)]
    
    for s in my_string :
        if s.isupper() :
            answer[ord(s)-ord('A')] += 1
        else :
            answer[ord(s)-ord('a')+ord('Z')-ord('A')+1] += 1
        
    return answer