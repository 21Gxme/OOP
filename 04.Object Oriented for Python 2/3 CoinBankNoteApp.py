class Coin_and_Banknote:
    def __init__(self,amount):
        self.amount = amount
        self.banknote = [1000, 500, 100, 50, 20]
        self.coin = [10, 5, 2, 1]
        self.banknote_amount = []
        self.coin_amount = []
        self.banknote_amount = self.get_banknote_amount()
        self.coin_amount = self.get_coin_amount()
        self.print_banknote()
        self.print_coin()

    def get_banknote_amount(self):
        for i in self.banknote:
            self.banknote_amount.append(self.amount//i)
            self.amount = self.amount % i
        return self.banknote_amount

    def get_coin_amount(self):
        for i in self.coin:
            self.coin_amount.append(self.amount//i)
            self.amount = self.amount % i
        return self.coin_amount

    def print_banknote(self):
        for i in range(len(self.banknote)):
            if self.banknote_amount[i] != 0:
                print(f'You get {self.banknote_amount[i]} of {self.banknote[i]} Baht Banknote')

    def print_coin(self):
        for i in range(len(self.coin)):
            if self.coin_amount[i] != 0:
                print(f'You get {self.coin_amount[i]} of {self.coin[i]} Baht Coin')

    def toString(self):
        return f'Banknote = {self.banknote_amount} Coin = {self.coin_amount}'


c = int(input('Input amount : '))
Tranfer(c)
