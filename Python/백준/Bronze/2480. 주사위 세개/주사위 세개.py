a,b,c = map(int,input().split(' '))
nums = [a,b,c]
num_dict = {}
for i in nums :
    try :
        num_dict[i] += 1
    except :
        num_dict.update({i : 1})
reverse_dict = {v:k for k,v in num_dict.items()}
if len(num_dict) == 1 :
    print(10000+reverse_dict[max(reverse_dict)]*1000)
elif len(num_dict) == 2 :
    print(1000+reverse_dict[max(reverse_dict)]*100)
else :
    print(max(num_dict)*100)