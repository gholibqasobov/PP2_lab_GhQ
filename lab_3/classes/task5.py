class account:
    owner = None
    balance = 0

    def deposit(self, deposit):
        self.balance += deposit
        print("Completed Successfully!")

    def withdraw(self, withdraw):
        if self.balance - withdraw >= 0:
            self.balance -= withdraw
            print("Completed Successfully!")
        else:
            print("You don't have enough money to withdraw!")


owner1 = account()

owner1.deposit(500)
owner1.withdraw(504)
