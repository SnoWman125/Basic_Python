import os

directory = {'myproject': ['settings', 'mainapp', 'adminapp', 'authapp']}
try:
    for dir, folder in directory.items():
        for f in folder:
            data = os.path.join(dir, f)
            os.makedirs(data)
except FileExistsError:
    print('File exist')
