def thesaurus(*args):
    my_dict = {}
    for i in args:
        if i[0] not in my_dict:
            my_dict[i[0]] = []
        my_dict[i[0]].append(i)
    print(my_dict)
thesaurus('Ivan', 'Natasha', 'Sergey', 'Irina', 'Vldaimir', 'Alex', 'Artem')