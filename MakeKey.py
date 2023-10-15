f=open("alphabet.txt","r")

L = [[i,0] for i in range(26)] 

Plain=f.read()
Plain = Plain.lower()

for c in Plain:
    if c.isalpha():
        L[ord(c)-97][1]+=1
        
f2=open("key.txt","w")

for i in range(26):  
    f2.write(f"{chr(L[i][0]+65)} = {L[i][1]}\n")

f.close() 
f2.close()

