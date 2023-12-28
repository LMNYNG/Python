def solution(keymap, targets):
    answer=[]
    map={}
    for keys in keymap:
        for i, k in enumerate(keys):
            if k in map:
                if map[k]>i+1:
                    map[k]=i+1
            else:
                map[k]=i+1
    for target in targets:
        sum=0
        for t in target:
            if t in map:
                sum+=map[t]
            else:
                sum=-1
                break
        answer.append(sum)
    return answer
