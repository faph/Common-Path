Common Path
===========

Python package to evaluate the most common (file) path from a list of paths.

Say you have a typical file history list::

>>> history = [
...     r'C:\Users\Adam Smith\Documents\doc1.txt',
...     r'C:\Users\Adam Smith\Documents\doc2.txt',
...     r'D:\doc4.txt',
...     r'C:\Users\Adam Smith\Documents\doc3.txt',
...     r'C:\Users\Adam Smith\Documents\Folder\image.jpg'
... ]

You want to know the most common path :file:`C:\Users\Adam Smith\Documents`, ignoring the occasional unusual path
:file:`D:\`.

>>> from commonpath import CommonPath
>>> CommonPath(history).natural()
'C:\\Users\\Adam Smith\\Documents'

Licence
-------

Distributed under the `MIT licence <LICENSE>`_.
