def solution(bandage, health, attacks):
    maxhealth=health
    inarow=0
    flag=0
    for a in range(attacks[-1][0]):
        print(f"******************TURN{a+1}******************")
        for i in range(len(attacks)):
            if((a+1)==attacks[i][0]):
                flag=1
                health-=attacks[i][1]
                inarow=0
                print(f"[Attacked!]now your health point is {health}")
                if (health<=0):
                    return -1
        if(flag==0):
            health+=bandage[1];
            inarow+=1
            print(f"[Healed!]now your health point is {health}")
            if (inarow%bandage[0]==0):
                health+=bandage[2];
                print(f"[In a Row Healed!]now your health point is {health}")
            if (health>maxhealth):
                health=maxhealth
                print(f"####[Result]now your health point is {health}####")
        flag=0
        
    return health
        
