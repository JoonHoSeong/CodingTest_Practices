s = int(input())
c = 0
while s >=3 :
    if s%5 == 0:
        c += s//5
        s = 0
        break
    s -= 3
    c += 1
if s != 0 :
    print(-1)
else :
    print(c)


