def solution(today, terms, privacies):
    answer=[]
    td=list(map(int,today.split(".")))
    for i, date in enumerate(privacies):
        for t in terms:
            if(date[-1]==t[0]):
                temp=list(map(int,date[:-1].split(".")))
                temp[1]+=int(t[2:])
                if(temp[1]>12):
                    temp[0]+=temp[1]//12
                    temp[1]=temp[1]%12
                if(temp[1]==0):
                    temp[0]-=1
                    temp[1]=12
                if ((temp[0]<td[0]) or (temp[0]<=td[0] and temp[1]<td[1]) or (temp[0]<=td[0] and temp[1]<=td[1] and temp[2]<=td[2])):
                    print(f"remian{temp})")
                    answer.append(i+1)
                else:
                    print(f"expired{temp}")

    return answer
                
