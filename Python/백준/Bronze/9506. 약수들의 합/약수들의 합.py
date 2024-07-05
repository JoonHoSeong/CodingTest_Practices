while True :
    num = int(input())
    if num == -1 :
        break
    nums = []
    for i in range(1,num) :
        if num%i == 0 :
            nums.append(i)
    if num == sum(nums) :
        print(f"{num} =",end='')
        for i,n in enumerate(nums) :
            if i+1 != len(nums) :
                print(f" {n} ", end='+')
            else :
                print(f" {n}")
    else :  
        print(f"{num} is NOT perfect.")