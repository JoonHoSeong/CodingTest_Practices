length = int(input())
num_list1 = list(map(int, input().split(' ')))
num_list2 = list(map(int, input().split(' ')))
num_list1.sort()
num_list2.sort(reverse=True)
answer = 0
for i in range(length) :
    answer = answer + (num_list1[i]*num_list2[i])
print(answer)