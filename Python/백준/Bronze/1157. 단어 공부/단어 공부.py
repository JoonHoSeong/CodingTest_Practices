word = input()
alpa = {}
for w in word.upper() :
    if w in alpa :
        alpa[w] += 1
    else :
        alpa.update({w : 0})
temp = [v for k,v in alpa.items()]
if temp.count(max(temp)) > 1 :
    print('?')
else :
    for k,v in alpa.items() :
        if v == max(temp) :
            print(k)