answer = 0
for _ in range(int(input())) :
    s = input()
    temp = []
    previous = ''
    for i in s :
        if i in temp and previous != i:
            answer -= 1
            break
        elif i not in temp :
            temp.append(i)
            previous = i
    answer += 1
if answer < 0 :
    print(0)
else :
    print(answer)
        