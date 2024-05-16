nums = input()
try :
    nums = nums.split('-')
    minus_num = 0
    for n in nums[1:] :
        if '+' in n :
            temp = list(map(int,n.split('+')))
            for t in temp :
                minus_num += t
        else :
            
            minus_num += int(n)
    plus = sum(list(map(int, nums[0].split('+'))))
    print(plus-minus_num)
except :
    print(sum(list(map(int,nums.split('+')))))