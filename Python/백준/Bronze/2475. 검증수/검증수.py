a,b,c,d,e = map(int,input().split(' '))
temp = [a,b,c,d,e]
temp = [i*i for i in temp]
print(sum(temp)%10)