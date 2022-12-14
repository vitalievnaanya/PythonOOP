class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.keys_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys_idx >= len(self.keys):
            raise StopIteration

        key = self.keys[self.keys_idx]
        value = self.dictionary[key]
        self.keys_idx += 1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)