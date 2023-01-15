def make_bold(func):
    def decorator(*args):
        result = f'<b>{func(*args)}</b>'
        return result
    return decorator


def make_italic(func):
    def decorator(*args):
        result = f'<i>{func(*args)}</i>'
        return result
    return decorator


def make_underline(func):
    def decorator(*args):
        result = f'<u>{func(*args)}</u>'
        return result
    return decorator


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))