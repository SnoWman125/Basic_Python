lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
item = 0
n_lst = []
while item < len(lst):
    if lst[item].isdigit():
        n_lst.extend(['"', lst[item].zfill(2), '"'])
        item += 1
    elif lst[item][0] in '+-' and lst[item][1:].isdigit():
        n_lst.extend(['"', lst[item][0], lst[item][1:].zfill(2), '"'])
        item += 1
    else:
        n_lst.append(lst[item])
        item += 1
print(n_lst)




