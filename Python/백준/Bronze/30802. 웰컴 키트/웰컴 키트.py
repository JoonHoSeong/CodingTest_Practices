nums = int(input())
shirts = list(map(int, input().split()))
t, p = map(int,input().split())

t_num = 0
for i in shirts :
    t_num += ((i-1)//t + 1)
    
print(t_num)
print(nums//p, nums%p)
