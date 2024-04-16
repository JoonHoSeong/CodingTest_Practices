for i in range(int(input())) :
    answer = 0
    ox = input().split('X')
    try :
        ox.remove('')
    except :
        pass
    for j in ox :
        for x in range(len(j)) :
            answer+= x+1
    print(answer)
    