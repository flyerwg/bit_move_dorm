import os, re, sys

path_block = ['.git', 'build']
suffix_block = ['md', 'py']
suffix_img = ['jpg', 'jpeg', 'png', 'bmp']

webpage_root = 'https://flyerwg.github.io/bit_move_dorm/'
github_root = 'https://github.com/flyerwg/bit_move_dorm/tree/master/'

UNITS = 'KMGT'
def strsize(x):
    unit='B'
    for du in UNITS:
        if x < 10:
            return '%.2f %s' % (x, unit)
        if x < 1000:
            return '%.1f %s' % (x, unit)
        unit = du + 'B'
        x /= 1024.0
    return '%g %s' % (x, unit)
