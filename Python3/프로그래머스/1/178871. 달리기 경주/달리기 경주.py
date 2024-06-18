def solution(players, callings):
    player = {player : rank for rank, player in enumerate(players)}
    rank = {rank : player for rank, player in enumerate(players)}
    
    for c in callings :
        r = player[c]
        player[rank[r]], player[rank[r-1]] = player[rank[r-1]], player[rank[r]]
        rank[r], rank[r-1] = rank[r-1], rank[r]
    
    return list(rank.values())