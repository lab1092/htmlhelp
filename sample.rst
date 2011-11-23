:orphan:

========
サンプル
========

http://docutils.sourceforge.net/docs/ref/rst/directives.html から。


Admonitions
====================================


Specific Admonitions
---------------------------

こんな風に書きます。
::

   
   .. DANGER::
      Beware killer rabbits!

表示例:

.. attention::
   注目

.. caution::
   注意

.. danger::
   危険

.. error::
   エラー

.. hint::
   ヒント

.. important::
   重要

.. note::
   ノート

.. tip::
   tips

.. warning::
   警告


Generic Admonition
---------------------------

タイトルと本文をクラスでくくった形になります。

::

   <document source="test data">
   <admonition classes="admonition-and-by-the-way">
      <title>
         And, by the way...
      <paragraph>
         You can make up your own admonition too.


.. admonition:: And, by the way...

   You can make up your own admonition too.



Container
---------------------------

:: 
   .. container:: custom

      This paragraph might be rendered in a custom way.


.. container:: custom

   This paragraph might be rendered in a custom way.


.. container:: custom-right

   This paragraph might be rendered in a custom way.

.. container:: custom-center

   This paragraph might be rendered in a custom way.

