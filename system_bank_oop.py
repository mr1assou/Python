"""
Write Python Program to Simulate a Bank Account with Support for depositMoney,
withdrawMoney and showBalance Operations
# Example usage
savings_account = BankAccount("Dupont")
savings_account.deposit_money(3500)
savings_account.show_balance()
savings_account.withdraw_money(1500)
savings_account.show_balance()
output
Dupont has deposited an amount of 3500.0 dollars
Dupont has a balance of 3500.0 dollars
Dupont has withdrawn an amount of 2000.0 dollars
Dupont has a balance of 2000.0 dollars    
"""
class BankAccount:
    bank={}
    def __init__(self,name_account):
        self.__name_account=name_account
        BankAccount.bank[self.__name_account]={'deposit_money':0000,'show_money':0000,'withdraw_money':0000,'show_balance':0000}
    def deposit_money(self,new_money):
        BankAccount.bank[self.__name_account]['deposit_money']+=new_money
        BankAccount.bank[self.__name_account]['show_money']=BankAccount.bank[self.__name_account]['deposit_money']
        return f"{self.__name_account} has deposited an amount  {BankAccount.bank[self.__name_account]['deposit_money']} of  dollars"
    def withdraw_money(self,pull_amount):
        BankAccount.bank[self.__name_account]['show_money']-=pull_amount
        BankAccount.bank[self.__name_account]['withdraw_money']+=pull_amount
        return f"{self.__name_account} has withdrawn an amount of {pull_amount} dollars"
    def show_balance(self):
        return f"{self.__name_account} has balance {BankAccount.bank[self.__name_account]['show_money']}"
#create object
obj1=BankAccount("Marwane")
print(obj1.deposit_money(3500))
print(obj1.show_balance())
print(obj1.withdraw_money(1500))
print(obj1.show_balance())
print(BankAccount.bank)
