#!/usr/bin/python3

'''Auto generate files for website support.
View https://flyerwg.github.io/bit_move_dorm/ to test the effect.
'''

from common import *

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
            filesize = os.path.getsize(os.path.join(path, target))
            size_str = strsize(filesize)
            webpage_url = webpage_path + target
            github_url = github_path + target
            f.write(f'文件大小：{size_str}，[下载]({webpage_url})，[在Github中查看]({github_url})\n\n')
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
