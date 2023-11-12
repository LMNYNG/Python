def solution(lines):
    start=101
    end=-101
    lines.sort(key=lambda x:(x[0],-x[1]))

    for i in range(3):
        for j in range(3):
            if i==j: continue
            if (lines[i][0] <= lines[j][0]) and (lines[i][1] > lines[j][0]): 
                start=min(lines[j][0],start)
                if lines[i][1]>=lines[j][1]:
                    end=max(lines[j][1],end)
                else:
                    end=max(lines[i][1],end)
    if start!=101:
        if lines[1][1]<lines[2][0]:
            answer=end-start-(lines[2][0]-lines[1][1])
        else:
            answer=end-start
    else:
        answer=0

    return answer
