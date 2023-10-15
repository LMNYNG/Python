f = open("key.txt","r")
L = [[i,0] for i in range(26)]
L2 = f.read().split("\n")
for i in range(26):   
    L[i][1]=int(L2[i].split()[2])
    
f2 = open("alphabet.txt","r")

f3=open("encrypted.txt","w",encoding="UTF-8")

L.sort(key=lambda x:x[1])

Plain = f2.read()
Plain = Plain.lower()

for c in Plain:
    if c.isalpha():
        f3.write(f"{chr(L[ord(c)-97][0]+97)}")
    else:
        f3.write(c)
f.close()
f3.close()

