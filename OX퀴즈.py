def solution(quiz):
    answer=[]
    a=list(map(lambda x: x.split("="),quiz))

    for b in a:
        if eval(b[0])==int(b[1]): 
            answer.append("O")
        else:
            answer.append("X")
    return answer
