for _ in range(int(input())) :
    h, w, n = map(int, input().split(' '))
    room_list = []
    room_num = 1
    for j in range(w) :
        for i in range(h) :
            room_num += 100
            room_list.append(room_num)
        room_num -= h*100
        room_num += 1
    print(room_list[n-1])
    