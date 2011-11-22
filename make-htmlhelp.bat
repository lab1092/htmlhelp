set pycmd=C:\python26\python.exe


call .\make.bat htmlhelp

rem 日本語ヘルプ作成のために実行

%pycmd% _cv_iso10646h.py
%pycmd% _cv_hhx.py
%pycmd% _cv_hhp.py

echo 日本語ヘルプのための変換が終わりました。

echo ヘルプファイルをコンパイルします。

rem chmコンパイラは以下を指定。
rem "C:\Program Files\HTML Help Workshop\hhc.exe"

%pycmd% _runhhc.pyw

pause
