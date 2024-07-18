n = int(input())
for i in range(0,n) :
    print('*'*(i+1), ' '*(n-i-1)*2,'*'*(i+1),sep='')
for i in range(n-1,0,-1) :
    print('*'*(i), ' '*(n-i)*2,'*'*(i),sep='')