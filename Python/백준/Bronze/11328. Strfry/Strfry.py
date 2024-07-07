for _ in range(int(input())) :
    s1, s2 = input().split(' ')
    if len(s1) != len(s2) :
        print('Impossible')
        continue
    temp = True
    s1 = list(s1)
    for i in s2 :
        if i not in s1 :
            temp = False
            break
        s1.pop(s1.index(i))
    if temp :
        print('Possible')
    else :
        print('Impossible')
        