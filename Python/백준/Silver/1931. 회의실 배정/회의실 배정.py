import sys
time_list = []
for _ in range(int(sys.stdin.readline())) :
    s,e = map(int,sys.stdin.readline().split(' '))
    time_list.append([s, e])
time_list.sort(key = lambda x : [x[1], x[0]])

answer = 0
end_time = 0
for t in time_list :
    if t[0] >= end_time :
        answer += 1
        end_time = t[1]
print(answer)
        