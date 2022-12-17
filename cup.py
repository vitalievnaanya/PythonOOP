class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
        self.left_space = self.size - quantity

    def fill(self, qty):
        if qty <= self.left_space:
            self.left_space -= qty

    def status(self):
        return self.left_space


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())