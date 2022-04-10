import os
import shutil
dir = 'myproject'
sample_lst = []
for root, dirs, files in os.walk(dir):
    for file in files:
        if '.html' in file:
            sample_lst.append(os.path.join(root, file))
print(sample_lst)
if not os.path.exists('templates'):
    os.mkdir('templates')
for sample in sample_lst:
    folder = os.path.join('templates', os.path.basename(os.path.dirname(sample)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(sample))
    shutil.copy(sample, save_path)



