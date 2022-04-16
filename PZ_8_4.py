from functools import wraps

def correct(check_correct):
    def val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if check_correct(*args):
                return func(*args)
            else:
                raise ValueError(*args)
        return wrapper
    return val_checker


@correct(lambda x: x > 0)
def cube(num):
    """Вычисляет куб числа"""

    return num ** 3

number = cube(5)
print(f'{number} --- {cube.__name__} --- {cube.__doc__}')