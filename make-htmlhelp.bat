set pycmd=C:\python26\python.exe


call .\make.bat htmlhelp

rem ���{��w���v�쐬�̂��߂Ɏ��s

%pycmd% _cv_iso10646h.py
%pycmd% _cv_hhx.py
%pycmd% _cv_hhp.py

echo ���{��w���v�̂��߂̕ϊ����I���܂����B

echo �w���v�t�@�C�����R���p�C�����܂��B

rem chm�R���p�C���͈ȉ����w��B
rem "C:\Program Files\HTML Help Workshop\hhc.exe"

%pycmd% _runhhc.pyw

pause
