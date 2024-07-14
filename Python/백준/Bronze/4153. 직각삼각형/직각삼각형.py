while True :
    nums = list(map(int,input().split()))
    if max(nums) == 0 :
        break
    nums = sorted(nums)
    if  nums[0]**2 + nums[1]**2 == nums[2]**2 :
        print('right')
        continue
    print('wrong')