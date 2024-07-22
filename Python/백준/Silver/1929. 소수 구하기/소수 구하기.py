a,b = map(int,input().split())

if a < 2:
    a = 2
for i in range(a,b+1) :
    t = True
    for j in range(2,int(i**0.5)+1) :
        if i%j == 0 :
            t = False
            break
    if t :
        print(i)