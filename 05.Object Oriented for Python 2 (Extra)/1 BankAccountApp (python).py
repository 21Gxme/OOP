class sam:

    def __init__(self):
        self.accountID = accountID
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        f'{self.accountID}, {self.balance}'


accountID = input("Enter account ID: ");

balance = float(input("Enter balance: "))


class pat:

    def __init__(self):
        self.accountID = accountID
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self):
        f'{self.accountID}, {self.balance}'




