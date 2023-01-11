class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iterations = 0
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration
        result = self.start
        self.start += self.step
        self.iterations += 1
        return result


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)