class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.num = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < 0:
            raise StopIteration
        result = self.num
        self.num -= 1
        return result


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")