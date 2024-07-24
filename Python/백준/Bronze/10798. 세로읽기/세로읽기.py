s = []
max_length = 0
for _ in range(5) :
    temp = list(input())
    s.append(temp)
    if max_length < len(temp) : max_length=len(temp)
for i in range(max_length) :
    for j in range(5) :
        try :
            print(s[j][i],end='',)
        except :
            pass