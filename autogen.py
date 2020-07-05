#!/usr/bin/python3

'''Auto generate files for website support.
View https://flyerwg.github.io/bit_move_dorm/ to test the effect.
'''

import os

path_block = ['.git']
suffix_block = ['md', 'py']
suffix_img = ['jpg', 'jpeg', 'png', 'bmp']

webpage_root = 'https://flyerwg.github.io/bit_move_dorm/'
github_root = 'https://github.com/flyerwg/bit_move_dorm/tree/master/'

def gen_index(path):
    'Generate index file for the dir *path*'
    filename = os.path.join(path,'README.md')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f'## {path}\n\n')
        targets = []
        for target in sorted(os.listdir(path)):
            name, suffix = target.rsplit('.', 1)
            suffix = suffix.lower()
            if suffix in suffix_block: continue
            targets.append((target, name, suffix))
        target_count = len(targets)
        webpage_path = webpage_root + path + '/'
        github_path = github_root + path + '/'
        f.write(f'共{target_count}个文件，[在网页中查看]({webpage_path})，[在Github中查看]({github_path})\n\n')
        for target, name, suffix in targets:
            f.write(f'* [{name}](#{name})\n')
        f.write('\n')
        for target, name, suffix in targets:
            f.write(f'### {name}\n\n')
            if suffix in suffix_img:
                f.write(f'![{name}]({target})\n\n')
                continue
            f.write(f'[{target}]({target})\n\n')

def main():
    for path in os.listdir():
        if not os.path.isdir(path): continue
        if path in path_block: continue
        gen_index(path)

if __name__ == '__main__':
    main()
