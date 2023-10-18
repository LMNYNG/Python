exp1 = input("다항식 입력:")
string = input("송신 문자열 입력:")
iterat = len(string)
temp = exp1.split('+')
temp2 = 0
origin = string
exp = []
code = ""
result =""

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ과정ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
for c in exp1:
    exp.append(c)

size = 1
if temp[0][0]=='x':
    size = int(temp[0][1:])+1

code2 = "0"*size

if exp1.split("+")[-1] == "1":
    code+="1"
else:
    code+="0"
    
for i in range(1,size):
    string +="0"

print(f"확장된 송신데이터는 [{string}]")

for i in range(0,size):
    code+='0'

for i in range(len(exp1.split('+'))):
    if(exp1.split('+')[i][0]=="1"):
        temp2+=10**0
    else:
        temp2+=10**int(exp1.split('+')[i][1:])
        
code=str(temp2)
print(f"다항코드는 [{code}]")

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ결과ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
result+=string[0:len(code)]

for i in range(iterat):
    if result[0]=="1":
        cal=bin(int(result,2)^int(code,2))[2:]
        
    else :
        cal=bin(int(result,2)^int(code2,2))[2:]
        
    result= "0"*(size-len(cal)) + cal
        
    if ((size+i) < len(string)):
        result = result[1:]+string[i+size]

result=result[1:]
print(f"체크섬 : [{result}]")
print(f"송신 데이터 : [{origin+result}]")




