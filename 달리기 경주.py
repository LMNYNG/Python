def solution(players, callings):
    player={}
    n=0
    for i in players:
        player[i]=n
        n=n+1
    for c in callings:
        index=player[c]
        pre_player=players[index-1]
        player[c]=player[c]-1
        player[pre_player]=player[pre_player]+1
        players[index-1]=players[index]
        players[index]=pre_player    
        
    return players
