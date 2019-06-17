import sys, re

from util import *

print('<html><head><title>kuraki</title></head><body>')

title = True
for block in blocks(sys.stdin):
    # 将block字符串中匹配到的子字符串替换成指定的字符串
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')

print('</body></html>')
