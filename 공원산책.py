def solution(park, routes):
    v_max=len(park)-1
    h_max=len(park[0])-1
    start=[]
    for i,p in enumerate(park):
        if "S" in p:
            start+=[i,p.find("S")]
            break
    print(f"v_max={v_max}, h_max={h_max}, start={start}")       
    for r in routes:
        v_temp=start[0]
        h_temp=start[1]
        iter=0
        print(f"v_temp={v_temp} h_temp={h_temp}")
        if r[0]=="N":
            while(iter<int(r[2])):
                iter+=1
                v_temp-=1
                if (v_temp < 0):
                    print("out!")
                    v_temp=start[0]
                    break
                if (park[v_temp][start[1]])=="X":
                    print("break!")
                    v_temp=start[0]
                    break
            start[0]=v_temp
            
        if r[0]=="S":
            while(iter<int(r[2])):
                iter+=1
                v_temp+=1
                if (v_temp > v_max):
                    print("out!")
                    v_temp=start[0]
                    break
                if (park[v_temp][start[1]])=="X":
                    print("break!")
                    v_temp=start[0]
                    break           
            start[0]=v_temp
            
        if r[0]=="E":
            while(iter<int(r[2])):
                iter+=1
                h_temp+=1
                if (h_temp > h_max):
                    print("out!")
                    h_temp=start[1]
                    break
                if (park[start[0]][h_temp])=="X":
                    print("break!")
                    h_temp=start[1]
                    break
            start[1]=h_temp
            
        if r[0]=="W":
            while(iter<int(r[2])):
                iter+=1
                h_temp-=1
                if (h_temp < 0):
                    print("out!")
                    h_temp=start[1]
                    break
                if (park[start[0]][h_temp])=="X":
                    print("break!")
                    h_temp=start[1]
                    break
            start[1]=h_temp
            
    return start
