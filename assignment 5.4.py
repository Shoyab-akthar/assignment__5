

class Account:
    def __init__(self, Title, Balance):
        self.Title, self.Balance = Title, Balance

class SavingsAccount(Account):
    def __init__(self, Title, Balance, InterestRate):
        super().__init__(Title, Balance)
        self.InterestRate = InterestRate

savings_account = SavingsAccount("Ashish", 5000, 5)

print("Title:", savings_account.Title)
print("Balance:", savings_account.Balance)
print("Interest Rate:", savings_account.InterestRate)
