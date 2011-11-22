==========================
トラブルシューティング
==========================

   :Version: 1.0.7
   :ext: pdf,blockdiagdiag,nwdiag
   :OS: Windows 

環境設定
====================================

easy_installって何ですか?
-------------------------

(これから書く)

PyPiって何ですか?
-----------------

(これから書く)


easy_install で ダウンロードエラーが起きる
--------------------------------------------------------------

正しいパッケージ名を指定して、"easy_install"コマンドを実行しても、
長い期間待って、以下のようなエラーが出る場合には、PyPiのページ
から、目的のパッケージを手動でダウンロードしてください。

.. code-block :: none

   Download error: [Errno 10060] 接続済みの呼び出し先が一定の時間を過ぎても正しく応
   答しなかったため、接続できませんでした。または接続済みのホストが応答しなかったため
   、確立された接続は失敗しました。 -- Some packages may not be found!
   No local packages or download links found for pytemplate
   Best match: None


.. note ::

   このとき、依存関係にあるパッケージも全てダウンロードすること。


PyPiからのパッケージダウンロードがZIP形式です。
--------------------------------------------------------------

拡張子を".egg"に変更して保存してください。



Sphinxの設定ファイルを作れません
------------------------------------

(これから書く)

PIL
---

Windows環境でPIL使う場合はバイナリ落としてくるのが楽。
ただし、FreeType2サポートのモジュールにしておくこと。

(これから書く)


なんちゃらdiagシリーズ
------------------------------

(これから書く)

その他のSphinxエクステンション
------------------------------

(これから書く)


rst2pdf
------------------------------

Sphinxを使ってPDF出力する場合にインストール、設定の変更を行なう
必要があります。

(これから書く)

Windows html help workshop
------------------------------

.chmファイルを作成できます。

コンパイル
====================================

conf.pyがありません
--------------------------

以下のエラーが出た場合には、conf.pyがありませんので、 `sphinx-quickstart.py` を再度
実行するか、 `conf.py` をバックアップからリストアしてください。

.. code-block :: none

   Error: Source directory doesn't contain conf.py file.

日本語を含むパス名について
--------------------------

`C:\\Documents and Settings\\mitsuda\\デスクトップ\\sandbox` でmakeしてみたら
エラーが出たなどの場合には、"パスに日本語が含まれている"からかも知れません。

コンパイル時のメッセージを注意深く眺めてみましょう。


以下のコマンドでは、ワーニングは出ましたが、コンパイルは終了しました。

   * make html
   * make htmlhelp

.. code-block :: none


   WARNING: the config value '__file__' is set to a string with non-ASCII character
   s; this can lead to Unicode errors occurring. Please use Unicode strings, e.g. u
   "Content".



以下のコマンドでは、エラーが出ました。


.. code-block :: none

   processing sandbox... [ERROR] pdfbuilder.py:129 'utf8' codec can't decode byte 0
   x83 in position 34: invalid start byte
   Traceback (most recent call last):
     File "C:\Python26\lib\site-packages\rst2pdf-0.16-py2.6.egg\rst2pdf\pdfbuilder.
   py", line 118, in write
       tgt_file = path.join(self.outdir, targetname + self.out_suffix)
     File "C:\Python26\lib\ntpath.py", line 108, in join
       path += "\\" + b
   UnicodeDecodeError: 'utf8' codec can't decode byte 0x83 in position 34: invalid
   start byte
  FAILED


その他
======

(これから書く)