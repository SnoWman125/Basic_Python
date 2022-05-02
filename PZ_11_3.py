class ElementError(Exception):
    def __init__(self, el):
        self.message = el if el else None

    def __str__(self):
        return f'Error: ElementError\n {self.message}' if self.message else 'Error: ElementError'


user_list = []


def get_num(x):
    if x[0] in '+-':
        return x[1:]


while True:
    user_inp = input('Enter a number: ')
    if user_inp == 'stop':
        break
    try:
        if user_inp.isdigit() or get_num(user_inp):
            user_list.append(int(user_inp))
        else:
            raise ElementError('Your number must be a digit.')
    except ElementError as e:
        print(e)
    else:
        print(f"Your number {user_inp} has been added to the list")

print(user_list)
