for i in range(1, 101):
    if 11 <= i <= 19:
        print('{} процентов'.format(i))
    elif i % 10 == 1:
        print('{} процент'.format(i))
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print('{} процента'.format(i))
    else:
        print('{} процентов'.format(i))
