# -*- coding: utf-8 -*-
#
# Sphinxから吐き出したhhpファイルを
# 日本語用に書き換えるよ（Win環境用)
# 
# 前提としてSphinxプロジェクト内で"make htmlhelp"していること
# (確認: Windows Vista/Python 2.6/Sphinx 1.0.7)

import os
import sys
import conf

# .hhp ファイルを変更の対象とする
cvpath = os.path.join(r'_build\htmlhelp' , conf.htmlhelp_basename + '.hhp' )


fi = open(cvpath,'r')

section = ''

buf = []
flg = [ 'Default Font=MS UI Gothic,8,128\n',\
        'Language=0x411\n' ]

while 1:
    line = fi.readline()

    # 終了条件
    if not line:
        break

    if line[0] == '[':
        section = line.strip()

    # 操作対象は[OPTIONS]セクションのみ
    if section == '[OPTIONS]':

        # [OPTIONS]セクション終わりの書きだし
        if line.strip() == '':
            for x in flg:
                if x != '' :
                    buf.append(x)

        # [OPTIONS]セクション中に書きだし
        if 'Default Font=' in line:
            buf.append('Default Font=MS UI Gothic,8,128\n')
            flg[0] = ''
            
        elif 'Language=' in line:
            buf.append('Language=0x411\n')
            flg[1] = ''
        else:
            buf.append(line)

    else:
        # [OPTIONS]セクション以外は1行そのまま書きだし
        buf.append(line)



fi.close()


fo = open(cvpath,'w')

for x in buf:
    fo.write(x)

fo.close()


