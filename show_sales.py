import sys

lst = sys.argv[1:]
with open('bakery.csv', 'r', encoding='utf-8') as bakery:
    line = bakery.readlines()
        if not lst:
            [print(i) for i in line]
        elif len(lst) == 1:
            print(line[int(lst[0]) - 1])
else:
    [print(line[i]) for i in range(int(lst[0]) - 1, int(lst[1]), 1)]
