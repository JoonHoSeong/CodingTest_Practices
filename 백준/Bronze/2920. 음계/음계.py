m = list(map(int,input().split(' ')))
temp = sorted(m)
temp2 = sorted(m,reverse=True)
if m == temp :
    print('ascending')
elif m == temp2 :
    print('descending')
else :
    print('mixed')