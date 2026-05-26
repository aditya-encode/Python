#create a class named Account with 2 attributes -balance & account no.
#create a method for debit ,credit & printing the balance

class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    
    def debit(self,amount):
        self.balance=self.balance-amount
        return self.balance
    def credit(self,amount):
         self.balance=self.balance+amount
         return self.balance

c1=Account(25000,123456789)
print(c1.debit(10000))
print(c1.credit(10000))
print(c1.account_no)
