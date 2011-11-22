# -*- coding: utf-8 -*-
#
# Sphinxから吐き出したhh[ck]ファイルを
# 日本語用のHTML(SJIS)に書き換えるよ（Win環境用)
# 
# 前提としてSphinxプロジェクト内で"make htmlhelp"していること
# Sphinx プロジェクトの言語指定は en
# (確認: Windows Vista/Python 2.6/Sphinx 1.0.7)

import os
import sys
import re

# conf.py をインポート
import conf


cvpaths = [os.path.join(r'_build\htmlhelp',conf.htmlhelp_basename + '.hhc') ,
           os.path.join(r'_build\htmlhelp',conf.htmlhelp_basename + '.hhk')]

# iso10646エンコードから、mcbsに変換
def foo(match):
    n = int(match.groups(0)[0])
    try:
        s = unichr(n).encode('mbcs')
    except:
        s= "?"
    return s

# 
p= re.compile(r'\&\#(\d*)\;')

for cvpath in cvpaths:

    fi = open(cvpath,'r')
    
    buf = []
    while 1:
        line = fi.readline()

        if not line:
            break

        buf.append(p.sub(foo,line))

    fi.close()


    fo = open(cvpath,'w')

    for x in buf:
        fo.write(x)

    fo.close()


