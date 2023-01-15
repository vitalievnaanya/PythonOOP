def type_check(type):
    def decorator(func):
        pass

        def wrapper(arg):
            if isinstance(arg, type):
                return func(arg)
            else:
                return 'Bad Type'

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))
