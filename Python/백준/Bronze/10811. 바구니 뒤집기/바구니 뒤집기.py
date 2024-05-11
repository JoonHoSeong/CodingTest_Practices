buket_num, change_num = map(int,input().split(' '))
buket_list = [i for i in range(1,buket_num+1)]
for i in range(change_num) :
    start, end = map(int, input().split(' '))
    temp = []
    for j in range(end-1,start-2, -1) :
        temp.append(buket_list[j])
    buket_list[start-1:end] = temp
print(' '.join(map(str,buket_list)))