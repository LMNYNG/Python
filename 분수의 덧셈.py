import math
def lcm(a,b):
    return (a * b) // math.gcd(a,b)

def solution(numer1, denom1, numer2, denom2):
    answer = [lcm(denom1,denom2)//denom1*numer1+lcm(denom1,denom2)//denom2*numer2,lcm(denom1,denom2)]
    gcd = math.gcd(answer[0],answer[1])
    return list(map(lambda x: x//gcd,answer))
