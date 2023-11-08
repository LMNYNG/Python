def solution(ineq, eq, n, m):   
    exp = (str(n)+ineq+eq+str(m)) if eq!="!" else (str(n)+ineq+str(m))
    return 1 if eval(exp)  else 0
