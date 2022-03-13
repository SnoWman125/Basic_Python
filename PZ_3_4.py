def thesaurus(*args):
    my_dict_ln = {}
    for i in args:
        split_i = i.split(' ')
        name = split_i[0]
        l_name = split_i[1]
        if l_name[0] not in my_dict_ln:
            my_dict_ln[l_name[0]] = {}
        if name[0] not in my_dict_ln[l_name[0]]:
            my_dict_ln[l_name[0]][name[0]] = []
        my_dict_ln[l_name[0]][name[0]].append(i)
    print(my_dict_ln)
thesaurus('Ivan Ivanov', 'Natasha Sikulina', 'Sergey Sergeev', 'Irina Ivanova', 'Vldaimir Serov', 'Alex Nikulin', 'Artem Noshkin')
