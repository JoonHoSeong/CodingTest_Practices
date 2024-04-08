str = input()
answer = ''
for s in str :
    if s.upper() == s :
        answer += s.lower()
    else :
        answer += s.upper()
        
print(answer)
