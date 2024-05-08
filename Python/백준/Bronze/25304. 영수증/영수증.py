total = int(input())
temp = 0
for i in range(int(input())) :
    money, num = map(int,input().split(' '))
    temp += money*num
if total == temp :
    print('Yes')
else :
    print('No')