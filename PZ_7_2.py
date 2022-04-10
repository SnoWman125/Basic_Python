import os
import yaml

hierarchy = {'myproject': [
    {'settings': ['__init__.py', 'dev.py', 'prod.py']},
    {'mainapp':  ['__init__.py', 'models.py', 'views.py', {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
    {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{'authapp': ['base.html', 'index.html']}]}]}
]
}
with open('dict.yalm', 'w') as f:
    yaml.dump(hierarchy, f)
with open('dict.yalm', 'r') as f:
    directory = yaml.safe_load(f)

def create_dir(directory):
    for dir, folders in directory.items():
        if os.path.exists(dir):
            print(f'{dir} exist')
        else:
            os.mkdir(dir)
        os.chdir(dir)
        for folder in folders:
            if isinstance(folder, dict):
                create_dir(folder)
            else:
                if '.' in folder:
                    with open(folder, 'w') as f:
                        f.write('')
    os.chdir('..')

create_dir(directory)