peoplenum = int(input())
time_list = list(map(int,input().split(' ')))
time_list.sort()
temp = 0
answer = 0
for t in time_list :
    temp += t
    answer += temp
print(answer)