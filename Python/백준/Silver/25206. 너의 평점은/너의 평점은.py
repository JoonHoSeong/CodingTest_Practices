total_num = .0
total_score = .0
while(1) :
    try :
        _, w, n = input().split(' ')
        if n != 'P' :
            w = float(w)
            if n == 'A+' :
                total_score += 4.5*w
            elif n == 'A0' :
                total_score += 4.0*w
            elif n == 'B+' :
                total_score += 3.5*w
            elif n == 'B0' :
                total_score += 3.0*w
            elif n == 'C+' :
                total_score += 2.5*w
            elif n == 'C0' :
                total_score += 2.0*w
            elif n == 'D+' :
                total_score += 1.5*w
            elif n == 'D0' :
                total_score += 1.0*w
            elif n == 'F' :
                pass
            total_num += w
    except :
        break
print(total_score/total_num)