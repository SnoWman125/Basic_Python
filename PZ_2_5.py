lst = [10, 51.1, 15, 0.15, 25.4, 8, 78.4, 390, 28.14, 124.78]
item_part = []
final_list = []
for item in lst:
    if '.' not in str(item):
        final_list.extend([item, 'руб. 00 коп.'])
    else:
        item_part = str(item).split('.')
        final_list.extend([str(item_part[0]), 'руб.', str(item_part[1]).zfill(2), 'коп.'])
print(''.join(str(final_list)))

print('#' * 100)
# Вывести цены, отсортированные по возрастанию, новый список не создавать
print(lst, id(lst))
lst.sort()
print(lst, id(lst))

print('#' * 100)
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
lst.reverse()
n_lst = []
for item in lst:
    n_lst.append(item)
print(n_lst)

print('#' * 100)
# Вывести цены пяти самых дорогих товаров.
print(n_lst[:-1][:5])

