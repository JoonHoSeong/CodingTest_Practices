

def test() :
    s = input()
    if s[0] == ')' :
        return 'NO'
    else :
        temp = []
        for i in s :
            if i == '(' :
                temp.append(')')
            elif i == ')' :
                try : 
                    temp.pop()
                except :
                    return 'NO'
        if len(temp) == 0 :
            return 'YES'
        else : return 'NO'
            
for _ in range(int(input())) :
    print(test())
            