def solution(n):
    a=0
    for i in range(n):
        a+=1
        while("3" in str(a) or a%3==0):
            a+=1
    return a
