h,m = map(int,input().split(' '))
if m-45 >= 0 :
    print(h,m-45,sep=' ')
else :
    m = m -45 + 60
    h = h-1
    if h < 0 :
        h = h+24
    print(h,m,sep=' ')