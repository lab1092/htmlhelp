# -*- coding: utf-8 -*-
#
# run Windows Help Compiler
# (copy this file to sphinx project folder)

import os
import sys
import conf

# modify the path for your own environment
runpath = r'C:\Program Files\HTML Help Workshop'
exepath = os.path.join(runpath ,'hhc.exe')

# htmlfile folder
htmpath = r'_build\htmlhelp' 

# .hhp
cnffile = os.path.join(htmpath ,conf.htmlhelp_basename + '.hhp')

# .chm
chmfile = os.path.join(htmpath,conf.htmlhelp_basename + '.chm')

cmdline = ('"%s" %s' )% (exepath,cnffile)

os.popen(cmdline,'r')
sys.stdout.flush()

os.popen(chmfile,'r')
sys.stdout.flush()