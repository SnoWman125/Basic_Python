def type_logger(func):
    def tag_wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}:{type(arg)})', end=', ')
        markup = func(*args)
        return markup
    return tag_wrapper

@type_logger
def cube(*args):
    cube_lst = []
    for num in args:
        cube_lst.append(num ** 3)
    return cube_lst

print(cube(5, 3, 20))
