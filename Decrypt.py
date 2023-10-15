f = open("encrypted.txt","r")
f1 = open("key.txt","r")
f2 = open("decrypted.txt","w")

enc = f.read()

L = [[i,0] for i in range(26)]

L2 = f1.read().split("\n")

for i in range(26):   
    L[i][1]=int(L2[i].split()[2])

L.sort(key=lambda x:x[1])

for i in range(26):
    L[i][1]=i

L.sort(key=lambda x:x[0])

print(L)

for c in enc:
    if c.isalpha():
        f2.write(f"{chr(L[ord(c)-97][1]+97)}")
    else:
        f2.write(c)

f.close()
f1.close()
f2.close()
    
