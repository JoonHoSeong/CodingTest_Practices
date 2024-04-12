a = input()
answer = ''
for i in a :
    if i.upper() == i :
        answer += i.lower()
    else :
        answer += i.upper()
        
print(answer)