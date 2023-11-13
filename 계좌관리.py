class Account:
    AN={"1002-656":5000}
    def deposit(self,accountid, money):
        self.AN[accountid]+=money
        print(f"잔액은 {self.AN[accountid]}원 입니다.")
    def withdraw(self,accountid, money):
        a=self.AN[accountid]-money
        if(a>0):
            self.AN[accountid]=a
            print(f"{money}원 출력 완료. 잔액 {self.AN[accountid]}")
        else:
            print("잔액이 부족합니다")
            
print("1002-656 Account 생성")
account = Account()
str = input("계좌번호 입력 (종료, End 입력 시 종료)>>")

while((str!="종료") and (str!="End")):
    method = input("출금/입금 선택>>")
    if(method=="출금"):
        money= int(input("원하는 금액 입력>>"))
        account.withdraw(str, money)
    if(method=="입금"):
        money= int(input("원하는 금액 입력>>"))
        account.deposit(str, money)
    str = input("계좌번호 입력 (종료, End 입력 시 종료)>>")
else: print("종료합니다")
        
