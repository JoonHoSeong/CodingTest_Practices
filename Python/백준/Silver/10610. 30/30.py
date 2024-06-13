nums = []
for i in input() :
    nums.append(i)
if '0' in nums and sum(map(int,nums))%3 == 0 :
    nums = list(map(int,nums))
    nums.sort(reverse=True)
    nums = list(map(str,nums))
    print(''.join(nums))
else :
    print(-1)
        

