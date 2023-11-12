def solution(b):
    a=[]
    c=[]
    d=[]
    
    a.append([abs(b[0][0]-b[1][0])/abs(b[0][1]-b[1][1])])
    a.append([abs(b[2][0]-b[3][0])/abs(b[2][1]-b[3][1])])
    c.append([abs(b[0][0]-b[2][0])/abs(b[0][1]-b[2][1])])
    c.append([abs(b[1][0]-b[3][0])/abs(b[1][1]-b[3][1])])
    d.append([abs(b[0][0]-b[3][0])/abs(b[0][1]-b[3][1])])
    d.append([abs(b[1][0]-b[2][0])/abs(b[1][1]-b[2][1])])
   
    a=set(tuple(i)for i in a)
    c=set(tuple(i)for i in c)
    d=set(tuple(i)for i in d)

    return 1 if len(a)==1 or len(c)==1 or len(d)==1 else 0
