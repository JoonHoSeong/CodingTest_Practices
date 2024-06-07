def solution(cards1, cards2, goal):
    for g in goal :
        if g == cards1[0] or g == cards2[0] :
            if g in cards1 and len(cards1) > 1:
                cards1 = cards1[1:]
            elif g in cards2 and len(cards2) > 1:
                cards2 = cards2[1:]
        else :
            return "No"
    return "Yes"