class BankAccount:
    def __init__(self):
        self.savings = 0

    def deposit(self, amount: float):
        self.savings += amount

    def withdraw(self, amount: float):
        self.savings -= amount

    def get_value(self):
        return self.savings


class SavingsAccount(BankAccount):
    def __init__(self, percent: float = 0.1):
        super().__init__()
        self.percent = percent

    def collect_savings(self):
        self.deposit(self.savings * self.percent)


def test_collect_savings():
    tsa = SavingsAccount(0.2)
    tsa.deposit(1000)
    tsa.collect_savings()

    assert tsa.savings == 1200


if __name__ == '__main__':
    ba = BankAccount()
    ba.deposit(101.20)
    ba.withdraw(1.20)
    print(ba.get_value())

