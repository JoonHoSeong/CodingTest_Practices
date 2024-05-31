a = input()
answer = 0
if 'c=' in a :
    answer += a.count('c=')
    a = a.replace('c=', ' ')
if 'c-' in a :
    answer += a.count('c-')
    a = a.replace('c-', ' ')
if 'dz=' in a :
    answer += a.count('dz=')
    a = a.replace('dz=', ' ')
if 'd-' in a :
    answer += a.count('d-')
    a = a.replace('d-', ' ')
if 'lj' in a :
    answer += a.count('lj')
    a = a.replace('lj', ' ')
if 'nj' in a :
    answer += a.count('nj') 
    a = a.replace('nj', ' ')
if 's=' in a :
    answer += a.count('s=')
    a = a.replace('s=', ' ')
if 'z=' in a :
    answer += a.count('z=')
    a = a.replace('z=', ' ')
answer += len(a.replace(' ',''))
print(answer)