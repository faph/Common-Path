![Travis](https://img.shields.io/travis/faph/Common-Path.svg?style=flat-square)
![Coveralls](https://img.shields.io/coveralls/faph/Common-Path.svg?style=flat-square)
[![Conda](https://anaconda.org/faph/commonpath/badges/installer/conda.svg)](https://anaconda.org/faph/commonpath)
[![PyPI](https://img.shields.io/pypi/v/commonpath.svg?style=flat-square)](https://pypi.python.org/pypi/commonpath)

# Common Path

Python package to evaluate the most common file path from a list of paths.

Say you have a typical file history list:

```python
>>> history = [
...     'C:\\Users\\Adam Smith\\Documents\\doc1.txt',
...     'C:\\Users\\Adam Smith\\Documents\\doc2.txt',
...     'C:\\Users\\log.txt',
...     'D:\\doc4.txt',
...     'C:\\Users\\Adam Smith\\Documents\\doc3.txt',
...     'C:\\Users\\Adam Smith\\Documents\\Folder\\image.jpg'
... ]
```

You want to know the common path `C:\Users\Adam Smith\Documents`, ignoring the occasional unusual paths `C:\Users` and 
`D:\`:

```python
>>> import commonpath
>>> commonpath.natural(history)
'C:\\Users\\Adam Smith\\Documents'
```

Want to limit the path depth?

```python
>>> commonpath.natural(history, max_depth=3)
'C:\\Users\\Adam Smith'
```

If you really want to know the absolute *most* common path:

```python
>>> commonpath.most(history)
'C:\\Users'
```

## Licence

Distributed under the [MIT licence](LICENSE).
