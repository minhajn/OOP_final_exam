class Bank:
    def __init__(self) -> None:
        self.users = []
        
    def create_user(self, name):
        user = User(name)
        self.users.append(user)

    def bank_balance(self):
        total_balance = sum(user.balance for user in self.users)
        return total_balance

    def bank_loan(self):
        total_loan = sum(user.loan for user in self.users)
        return total_loan


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.balance = 0
        self.loan = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f'Deposited : {amount}')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f'Withdrawn : {amount}')
        else:
            self.history.append('Insufficient Balance.')

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit(amount)
            self.history.append(f'Transferred : {amount}')
        else:
            self.history.append('Insufficient Balance.')

    def check_available_balance(self):
        return f'Your available balance is: {self.balance}'
    
    def take_loan(self):
        loan_amount=self.balance*2
        self.deposit(loan_amount)
        self.history.append(loan_amount, "Loan")

    def check_history(self):
        return self.history


def main():
    Janata = Bank()
    Janata.create_user('Minhaz')
    Janata.create_user('Abedin')

    user1 = Janata.users[0]
    user2 = Janata.users[1]

    user1.deposit(5000)
    user1.transfer(200, user2)

    print(user1.check_available_balance())
    print(user2.check_history())
    print(user1.check_history())
    print(Janata.bank_loan())


if __name__ == "__main__":
    main()