class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.curr_num = self.start

    def __iter__(self):
        return self

    def __next__(self):
        value_to_return = self.curr_num
        self.curr_num += 1

        if value_to_return > self.end:
            raise StopIteration

        return value_to_return


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)