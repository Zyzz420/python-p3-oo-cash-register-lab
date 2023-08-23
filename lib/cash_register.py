class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, item, price, quantity=1):
        for _ in range(quantity):
            self.total += price
            self.items.append(item)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount of {self.discount}%, the new total is ${self.total:.2f}")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction_amount > 0:
            self.total -= self.last_transaction_amount
            self.items = self.items[:-1]
            self.last_transaction_amount = 0

    def get_total(self):
        return self.total

    def get_items(self):
        return self.items

    def reset_total(self):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0