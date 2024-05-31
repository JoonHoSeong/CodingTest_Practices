answer_list=[1,1,2,2,2,8]
nums = list(map(int, input().split(' ')))
for i in range(len(answer_list)) :
    print( answer_list[i] - nums[i], end=' ')