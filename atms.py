initial_balance=input('your current balance')
bank_name=input('your bank name')  
class atm:
    def __init__(self, balance, company):
        self.balance=int(balance)
        self.company=company
    def cashWithdrawl(self, amount):
        self.balance=self.balance-int(amount)
        print(amount,'cash_withdrawn')
    def balanceEnquiry(self):
        print(self.balance)
    def printbank(self):
        print(self.company)
def egg():
    my_atm=atm(initial_balance, bank_name)
    print('you can call cashWithdrawl [space] amount, balanceEnquiry or printbank anytime')
    m=input("enter detail")
    if(m=='balanceEnquiry'):
        print(my_atm.balance)
    if((m.find('cashWithdrawl'))>-1):
        x=m.split()
        my_atm.cashWithdrawl(x[1])
        print(my_atm.balance)
    if(m=='printbank'):
        my_atm.printbank()
g=0
while(g==0):
    egg()