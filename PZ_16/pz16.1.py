"""
Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
Добавьте методы для вычисления процентных начислений и снятия денег.
"""

class Bank:
    def __init__(self, amount=0, interest_rate=0):
        self.amount = amount
        self.interest_rate = interest_rate

    # ВЫЧИСЛИТЬ ПРОЦЕНТ
    def calculate_interest(self, years=1):
        interest = self.amount * (self.interest_rate / 100) * years
        return interest

    # CНЯТЬ ДЕНЬГИ
    def withdraw(self, withdrawal_amount):
        if withdrawal_amount <= 0:
            print("Сумма снятия должна быть положительной")
            return False
        if withdrawal_amount > self.amount:
            print(f"Недостаточно средств. Доступно: {self.amount}")
            return False
        self.amount -= withdrawal_amount
        print(f"Успешно снято: {withdrawal_amount}. Баланс на остатке: {self.amount}")
        return True

    # ВНЕСТИ ДЕНЬГИ
    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print("Сумма внесения должна быть положительной")
            return
        self.amount += deposit_amount
        print(f"Успешно внесено: {deposit_amount}. Новый баланс: {self.amount}")




bank_account = Bank(10000, 5)
print(f"Начальный баланс: {bank_account.amount}")
print(f"Процентная ставка: {bank_account.interest_rate}%")

interest = bank_account.calculate_interest(1)
print(f"Проценты за 1 год: {interest}")

bank_account.withdraw(3000)

bank_account.deposit(500)
