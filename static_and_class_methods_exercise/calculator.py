class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(initial, *args):
        result = initial
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(initial, *args):
        result = initial
        for x in args:
            result /= x
        return result

    @staticmethod
    def subtract(initial, *args):
        result = initial
        for x in args:
            result -= x
        return result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
