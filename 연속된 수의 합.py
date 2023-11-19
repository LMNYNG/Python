def solution(num, total):
    return ([a for a in range(((2*total//num)-(num-1))//2,((2*total//num)-(num-1))//2+num)])
