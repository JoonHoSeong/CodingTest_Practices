n = int(input())
for i in range(n) :
    num, s=input().split(' ')
    for j in s :
        for i in range(int(num)) :
            print(j,end='')
    print()