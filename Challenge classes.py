# For this challenge, create a bank account class that has two attributes:
# owner
# balance
# and two methods:
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance
class bankaccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def __str__(self):
        return f"owner : {self.owner} \nbalance {self.balance}"

    def deposit(self, deposit):
        self.balance += deposit
        print("Deposit accepted")

    def withdraw(self, withdrawal):
        if self.balance >= withdrawal:
            self.balance -= withdrawal
            print("Funds withdrawn")
        else:
            print('insufficient funds')


acct1 = bankaccount('Jose', 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1.withdraw(75))
