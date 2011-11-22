# -*- coding: utf-8 -*-
#
# Sphinxから吐き出したhtmlファイルを
# 日本語用のHTML(SJIS)に書き換えるよ（Win環境用)
# 
# 前提としてSphinxプロジェクト内で"make htmlhelp"していること
# Sphinx プロジェクトの言語指定は en
# (確認: Windows Vista/Python 2.6/Sphinx 1.0.7)

import os
import sys
import re

# "make htmlhelp" で出力されるディレクトリ
cvpath = r'_build\htmlhelp'


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

lines= os.popen("dir /B /A-D "+cvpath+"\\*.html","r")
sys.stdout.flush()

while 1:

    filename = lines.readline()
    filename = filename.rstrip()

    if not filename: break

    fi = open(cvpath+"\\"+filename,'r')

    buf = []
    
    while 1:
        line = fi.readline()

        if not line:
            break

        line = line.replace('content="text/html; charset=iso8859_1"','content="text/html; charset=shift-jis"')
        buf.append(p.sub(foo,line))

    fi.close()
    
    fo = open(cvpath+"\\"+filename,'w')
    
    for x in buf:
        fo.write(x)
    
    
    fo.close()


