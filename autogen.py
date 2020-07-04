#!/usr/bin/python3

'''Auto generate files for website support.
View https://flyerwg.github.io/bit_move_dorm/ to test the effect.
'''

import os

suffix_block = ['md', 'py']
suffix_img = ['jpg', 'jpeg', 'png', 'bmp']

def gen_index(path):
    'Generate index file for the dir *path*'
    filename = os.path.join(path,'README.md')
    with open(filename, 'w', encoding='utf-8') as f:
        for target in os.listdir(path):
            name, suffix = target.rsplit('.', 1)
            suffix = suffix.lower()
            if suffix in suffix_block: continue
            if suffix in suffix_img:
                f.write(f'![{name}]({target})\n\n')
                continue
            f.write(f'[{name}]({target})\n\n')

def main():
    for path in os.listdir():
        gen_index(path)

if __name__ == '__main__':
    main()
