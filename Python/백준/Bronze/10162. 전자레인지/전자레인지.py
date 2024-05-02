t= int(input())
a,b,c = 0,0,0
if t//300 > 0 :
    a += t//300
    t = t%300
if t//60 > 0 :
    b += t//60
    t = t%60
if t//10 > 0 :
    c += t//10
    t = t%10
if t == 0 :
    print(a,b,c,sep=' ')
else :
    print(-1)