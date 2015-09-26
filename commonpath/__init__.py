# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2015 Florenz A. P. Hollebrandse
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

from collections import defaultdict, Counter
from os.path import sep, normpath
import sys


class CommonPath(object):
    def __init__(self, paths):
        #: List of paths to analyse
        self.paths = list(map(normpath, paths))
        #: Default maximum path depth to analyse
        self.default_max_depth = sys.maxsize
        #: Most common path for different path depths
        self.most_common = self._most_common()

    def _most_common(self):
        split_paths = [p.split(sep) for p in self.paths]
        # Dict of list of unpacked paths with path depth level as keys
        # e.g. {0: ['', '', ''],
        #       1: ['/home', '/home', '/usr'],
        #       2: ['/home/user1', '/home/user1', '/usr/bin']}
        levels = defaultdict(list)
        for split_path in split_paths:
            for level, ele in enumerate(split_path):
                levels[level].append(sep.join(split_path[0:level + 1]))

        # List of tuples (most common path, count) by increasing path depth
        # e.g. [('', 3),
        #       ('/home', 2),
        #       ('/home/user1', 2)]
        return [Counter(level).most_common(1)[0] for level in levels.values()]

    def natural(self, max_depth=None):
        """
        Return the "natural" deepest common path.

        Incidental uncommon path names are ignored. A minimum number of common paths threshold is used, depending on the
        path depth, i.e. deeper path names are preferred as long as it is sufficiently common.

        :param max_depth: maximum path depth to analyse
        :type max_depth: int
        :return: common path
        :rtype: str
        """
        max_depth = max_depth or self.default_max_depth
        min_count = min(0.75 * len(self.paths), self.most_common[0][1])
        result = None
        for i, common in enumerate(self.most_common):
            if common[1] < round(min_count, 0) or i > max_depth - 1:
                break
            else:
                result = common[0]
                min_count *= 0.9
        return result

    def most(self, max_depth=None):
        """
        Return the most common path.

        The most common path is evaluated at increasing path depths. As soon as the frequency/count of the common path
        goes down, the path is returned.

        :param max_depth: maximum path depth to analyse
        :type max_depth: int
        :return: common path
        :rtype: str
        """
        max_depth = max_depth or self.default_max_depth
        max_count = 0
        result = None
        for i, common in enumerate(self.most_common):
            if common[1] < max_count or i > max_depth - 1:
                break
            else:
                max_count = common[1]
                result = common[0]
        return result