def solution(babbling):
    cnt=0
    babble=["aya","ye","woo","ma"]
    for i in range(len(babbling)):
        for j in babble:
            babbling[i]=babbling[i].replace(j," ")
    print(babbling)
    for i in babbling:
        if not i.strip(): cnt+=1
    return cnt
