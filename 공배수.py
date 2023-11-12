def solution(number, n, m):
    def GCD(a,b):
        if(b==0):
            return a
        else:
            return GCD(b,a%b)
        
    return 1 if number%(n*m//GCD(n,m))==0 else 0
