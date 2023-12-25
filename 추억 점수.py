def solution(name, yearning, photo):
    answer=[]
    dic={}
    for i,n in enumerate(name):
        dic[n]=yearning[i]
    print(dic)
    for i in photo:
        sum=0
        for j in i:
            if j in dic:
                sum+=dic[j]
        answer.append(sum)
    return(answer)
