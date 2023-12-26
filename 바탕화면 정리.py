def solution(wallpaper):
    x=[]
    y=[]
    answer=[]
    for i,wall in enumerate(wallpaper):
        for j,element in enumerate(wall):
            if element=="#":
                x.append(i)
                y.append(j)
    print(f"x={x}, y={y}")
    answer+=min(x),min(y),max(x)+1,max(y)+1
    return answer
