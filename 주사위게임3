def solution(a, b, c, d):
    origin=[a,b,c,d]
    changed=list(set(origin))
    if len(changed)==4:
        return changed[0]
    elif len(changed)==3:
        if origin.count(changed[0])==2:
            return changed[1]*changed[2]
        elif origin.count(changed[1])==2:
            return changed[0]*changed[2]
        else:
            return changed[0]*changed[1]
    elif len(changed)==2:
        if origin.count(changed[0])==3:
            return (10*changed[0]+changed[1])**2 
        elif origin.count(changed[1])==3:
            return (10*changed[1]+changed[0])**2 
        else:
            return (changed[0]+changed[1])*abs(changed[0]-changed[1]) 
    else:
        return 1111*changed[0]
