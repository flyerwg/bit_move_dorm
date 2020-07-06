#!/usr/bin/python3

'''Auto build files for release.
'''

from common import *
import urllib.request as request
import urllib.parse as parse

build_path = os.path.join('build', 'bit_move_dorm')
other_files = [('assets','css','style.css')]
threshold_size = 3 << 20

def download(url, filename, processor = None, encoding = 'utf-8'):
    print(f'downloading {url}')
    response = request.urlopen(url)
    html = response.read()
    if processor is not None:
        html = processor(html.decode(encoding)).encode(encoding)
    path, _ = os.path.split(filename)
    os.makedirs(path, exist_ok = True)
    with open(filename, 'wb') as f:
        f.write(html)

def common_processor(html):
    html = re.sub(r'style\.css\?v\=[0-9a-f]+"', 'style.css"', html)
    p1 = html.find('<footer ')
    p2 = html.find('</footer>')
    html = html[0:p1] + html[p2 + 9:]
    return html

def processor_root(html):
    'translate root link address'
    html = common_processor(html)
    html = html.replace('"/bit_move_dorm/','"./')
    html = html.replace('/">相关','/index.html">相关')
    return html

def processor_subdir(html):
    'translate subdir link address'
    html = common_processor(html)
    html = html.replace('"/bit_move_dorm/','"../')
    return html

def crawl_index(path, mode):
    'crawl Github page for the dir *path*'
    webpage_path = webpage_root + parse.quote(path) + '/'
    local_path = os.path.join(build_path, path)
    filename = os.path.join(local_path,'index.html')
    if not os.path.exists(filename):
        download(webpage_path, filename, processor_subdir)
    for target in sorted(os.listdir(path)):
        name, suffix = target.rsplit('.', 1)
        suffix = suffix.lower()
        if suffix in suffix_block: continue
        filename_from = os.path.join(path, target)
        filename_to = os.path.join(local_path, target)
        if os.path.exists(filename_to):
            os.remove(filename_to)
        if mode == 'size':
            filesize = os.path.getsize(filename_from)
            if filesize > threshold_size: continue
        if mode == 'img' and suffix not in suffix_img: continue
        with open(filename_from, 'rb') as f_from:
            with open(filename_to, 'wb') as f_to:
                f_to.write(f_from.read())

def main(mode = 'all'): # mode: all, size, img
    filename = os.path.join(build_path,'index.html')
    download(webpage_root, filename, processor_root)
    for names in other_files:
        quoted_names = map(parse.quote, names)
        webpage_path = webpage_root + '/'.join(quoted_names)
        local_path = os.path.join(build_path, *names)
        download(webpage_path, local_path)
    for path in os.listdir():
        if not os.path.isdir(path): continue
        if path in path_block: continue
        crawl_index(path, mode)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
