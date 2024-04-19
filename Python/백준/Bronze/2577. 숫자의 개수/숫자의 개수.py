a = int(input())
a *= int(input())
a *= int(input())
nums = {str(i):0 for i in range(10)}
for c in str(a) :
    nums[c] += 1
for c in nums :
    print(nums[c])