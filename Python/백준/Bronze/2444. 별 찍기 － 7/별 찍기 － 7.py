n = int(input())
for i in range(1,n+1) :
    print(' ' *(n-i) +'*' * (i*2-1))
for i in range(n-1,0,-1) :
    print(' ' *(n-i) +'*' * ((i-1)*2+1))