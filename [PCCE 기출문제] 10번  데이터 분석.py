def solution(data, ext, val_ext, sort_by):
    answer = []
    dictionary={"code":0, "date":1, "maximum":2, "remain":3}
    print(dictionary[ext])
    for i in range(len(data)):
        if(int(data[i][dictionary[ext]])<val_ext): answer.append(data[i])
    answer=sorted(answer, key=lambda x:x[dictionary[sort_by]])
    return answer
