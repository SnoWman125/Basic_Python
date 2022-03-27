src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Необходимо вывести те элементы, значения которых больше предыдущего

result = [src[i] for i in range(2, len(src)) if src[i] > src[i-1]]
print(result)

def gen(lst):
    for i in range(2, len(lst)):
        if lst[i] > lst[i-1]:
            yield lst[i]

gen_lst = gen(src)
print(*gen_lst)
